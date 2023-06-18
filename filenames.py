class Filenames:
    def __init__(self):
        self.filenames={}

    def add(self,message_chat_id,filename):
        self.filenames[message_chat_id]=filename

    def get(self,message_chat_id):
        return self.filenames[message_chat_id]

    def get_dict(self):
        return self.filenames

    def pop(self,message_chat_id):
        self.filenames.pop(message_chat_id)


