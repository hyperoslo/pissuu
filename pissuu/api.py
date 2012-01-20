import requests
import md5
import json

class IssuuAPI(object):

    def __init__(self, key, secret):
        """
        Initialize an API client with the given ``key`` and ``secret``.
        """
        self.key = key
        self.secret = secret

    def add_bookmark(self):
        """
        Add a bookmark.
        """
        raise NotImplementedError()

    def list_bookmarks(self):
        """
        List bookmarks.
        """
        raise NotImplementedError()

    def update_bookmark(self):
        """
        Update a bookmark.
        """
        raise NotImplementedError()

    def delete_bookmark(self):
        """
        Delete a bookmark.
        """
        raise NotImplementedError()

    def list_documents(self):
        """
        List documents for this user.
        """
        return self._query(
            url = 'http://api.issuu.com/1_0',
            action = 'issuu.documents.list'
        )

    def upload_document(self, file, title=None):
        """
        Upload the given ``file``.
        """
        response = self._query(
            url = 'http://upload.issuu.com/1_0',
            action = 'issuu.document.upload',
            data = {
                'file': file,
                'title': title
            }
        )

        return response['document']['documentId']

    def update_document(self):
        """
        Update a document.
        """
        raise NotImplementedError()

    def delete_document(self):
        """
        Delete a document.
        """
        raise NotImplementedError()

    def add_folder(self):
        """
        Create a folder.
        """
        raise NotImplementedError()

    def list_folders(self):
        """
        List folders.
        """
        raise NotImplementedError()

    def update_folder(self):
        """
        Update a folder.
        """
        raise NotImplementedError()

    def delete_folder(self):
        """
        Delete a folder.
        """
        raise NotImplementedError()

    def _query(self, url, action, data={}):
        """
        Low-level access to the Issuu API.
        """

        data.update({
            'apiKey': self.key,
            'format': 'json',
            'action': action
        })

        data['signature'] = self._sign(data)

        files = {}

        for key in data:
            if hasattr(data[key], 'read'):
                files[key] = data[key]

        for key in files:
            data.pop(key)

        response = requests.post(
            url = url,
            data = data,
            files = files
        )

        try:
            data = json.loads(response.content)['rsp']
        except ValueError:
            raise self.Error('API response could not be parsed as JSON')

        if data['stat'] == 'fail':
            raise self.Error(data['_content']['error']['message'])
        else:
            return data['_content']

    def _sign(self, data):
        """
        Create a signature of the given ``data``.
        """
        signature = self.secret

        data.update({
            'apiKey': self.key
        })

        keys = data.keys()

        for key in sorted(keys):
            if isinstance(data[key], (str, unicode)):
                signature += key + data[key]

        return md5.new(signature).hexdigest()

    class Error(StandardError):
        pass
