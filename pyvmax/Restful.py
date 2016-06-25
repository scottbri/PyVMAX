import requests
import json
import logging
import time

# Disable warnings from untrusted server certificates
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
except Exception:
    print("Ignore messages related to insecure SSL certificates")


class Restful:
    """Restful class implements network calls to communicate with REST API server
    Attributes:
        log (:obj:`logging`): logger object
    Args:
        base_url (str):  the ip and port # of api server
        username (str):  credentialed user of unisphere
        password (str):  the user's password
        verifySSL (Ture / False), optional:  verify SSL security cert or not
    """

    def __init__(self, base_url, username, password, verifySSL=False):
        self.url = base_url
        self.user = username
        self.password = password
        self.verify_ssl = verifySSL
        self.api_counter = 0
        self.api_start_time = 0
        self.api_end_time = 0
        self.api_timer = 0
        self.api_last_resp_time = 0

        # set the headers for how we want the response
        self.headers = {'content-type': 'application/json', 'accept':'application/json'}

        self.log = logging.getLogger('pyvmax')
        self.log.debug('Setting up Restful')

    def set_url(self, new_url):
        self.url = new_url

    def json_to_str(self, json_obj):
        """converts json to string

        Args:
            json_obj(any type convertable to string): esp dict, list string, requests response object
        Returns:
            string
        """
        return str(json.dumps(json_obj, sort_keys=False, indent=2))

    def timer_start(self):
        self.api_counter += 1
        self.api_start_time = int(round(time.time() * 1000))

    def timer_stop(self):
        self.api_end_time = int(round(time.time() * 1000))
        self.api_last_resp_time = (self.api_end_time - self.api_start_time)
        self.api_timer += self.api_last_resp_time

    @property
    def api_average_time(self):
        if self.api_counter > 0:
            return self.api_timer / self.api_counter
        else:
            return 0

    def get(self, target_url, payload=None):
        """ make the REST GET call to the public api

        Args:
            target_url(str): the full REST API URL
            payload(dict, optional): dict representing the json request payload
        Returns:
            dict():  could be empty
        """

        self.timer_start()
        try:
            if payload == None:
                response = requests.get(target_url,
                                        auth=(self.user, self.password),
                                        headers=self.headers,
                                        verify=self.verify_ssl)
            else: # payload is something
                response = requests.get(target_url,
                                        params=json.dumps(payload),
                                        auth=(self.user, self.password),
                                        headers=self.headers,
                                        verify=self.verify_ssl)

        except Exception:
            self.log.critical("Can't GET to API server URL:  " + target_url)
            self.log.critical("Exiting get")
            exit(1)

        self.timer_stop()

        #take the raw response text and deserialize it into a python object.
        try:
            response_object = json.loads(response.text)
        except Exception:
            self.log.warning("API GET did not return JSON response")
            self.log.warning(response.text)
            return dict()

        # this is a VMAX API peculiarity, that 'message' in the JSON means
        # the server is having issues, and the response can't be well made
        if 'message' in response_object:
            self.log.warning("API call" + target_url + " : server only responded with:")
            self.log.warning(self.json_to_str(response_object))
            response_object = dict()

        return response_object

    def post(self, target_url, request_object=None):
        """ make the REST POST call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict():  could be empty
        """

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        self.timer_start()
        try:
            response = timer_counter(requests.post(target_url,
                                                   data=json.dumps(request_object),
                                                   auth=(self.user, self.password),
                                                   headers=self.headers,
                                                   verify=self.verify_ssl))

            #take the raw response text and deserialize it into a python object.
            try:
                response_object = json.loads(response.text)
            except Exception:
                self.log.warning("API POST did not return JSON response")
                self.log.warning(response.text)
                self.timer_stop()
                return dict()
        except Exception:
            self.log.critical("Exception:  Can't POST to API server URL:  " + target_url)
            self.log.critical(self.json_to_strn(request_object))
            self.log.critical("Exiting POST")
            exit(1)

        self.timer_stop()
        return response_object


    def put(self, target_url, request_object=None):
        """ make the REST PUT call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict():  could be empty
        """

        #turn this into a JSON string
        request_json = json.dumps(request_object, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        self.timer_start()
        try:
            response = timer_counter(requests.put(target_url,
                                                  request_json,
                                                  auth=(self.user, self.password),
                                                  headers=self.headers,
                                                  verify=self.verify_ssl))
        except Exception:
            self.log.critical("Exception:  Can't PUT to API server URL:  " + target_url)
            self.log.critical(self.json_to_str(request_object))
            self.log.critical("Exiting PUT")
            exit(1)
        self.timer_stop()

        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(response.text)
        except Exception:
            self.log.warning("API PUT did not return JSON response")
            self.log.warning(response.text)
            return dict()
        return response


    def delete(self, target_url, request_object=None):
        """ make the REST DELETE call to the public api

        Args:
            target_url(str): the full REST API URL
            request_object(dict, optional): dict representing the json request payload
        Returns:
            dict():  could be empty
        """

        #turn this into a JSON string
        request_json = json.dumps(request_object, sort_keys=True, indent=4)

        #make the actual request, specifying the URL, the JSON from above,
        #standard basic auth, the headers and not to verify the SSL cert.
        self.timer_start()
        try:
            response = timer_counter(requests.delete(target_url,
                                                     request_json,
                                                     auth=(self.user, self.password),
                                                     headers=self.headers,
                                                     verify=self.verify_ssl))
        except Exception:
            self.log.critical("Exception:  Can't DELETE to API server URL:  " + target_url)
            self.log.critical(self.json_to_str(request_object))
            self.log.critical("Exiting DELETE")
            exit(1)

        self.timer_stop()
        #take the raw response text and deserialize it into a python object.
        try:
            response = json.loads(response.text)
        except Exception:
            self.log.warning("API DELETE did not return JSON response")
            self.log.warning(response.text)
            return dict()
        return response


