class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    """
    read the inbox for a user from the unread messages and mark them as read
        Args : 
        username : is the user whose inbox is to be read
        number : number of the unread messages that he need to read 
        
        :returns an list of strings containing the unread messages
        
    """
    def read_inbox(self, username: str, number=0) -> list:
        messages = self.boxes[username]
        if number == 0:
            number = len(messages)
        returnedMessages = []
        for i in range(number):
            if not messages[i]['read']:
                newMessage = {}
                newMessage['sender'] = messages[i]['sender']
                newMessage['body'] = messages[i]['body']
                returnedMessages.append(newMessage)
                messages[i]['read'] = True
        self.boxes[username] = messages

        return returnedMessages
    """
        search the inbox from the user mails and return the messages that's contains 
        a word for search
        
        :arguments
            username : is the user whose inbox is to be searched 
            body : is the sub message that we want to search it 
            
        :returns  an list with all the the messages containing a word for search
        
        Examples: 
            search_inbox("saleh" "python")
            and there an message = " in this semester i have an python  course " 
            :returns the whole messages  " in this semester i have an python  course"
            because python in the message 
            
            and also work for sub message like
            search_inbox("saleh" "py")
            :returns in this semester i have an python  course
    """
    def search_inbox(self, username: str, body: str) -> list:
        messages = self.boxes[username]
        searchedMessages = []
        for message in messages:
            if body in message['body']:
                searchedMessages.append(message['body'])
        return searchedMessages


if __name__ == '__main__':
    postOffice = PostOffice(["saleh", "roba"])
    postOffice.send_message("saleh", "roba", "love is wnat to ds", False)
    postOffice.send_message("saleh", "roba", "love2", False)
    postOffice.send_message("saleh", "roba", "love3", False)

    print(postOffice.search_inbox("roba", 'lo'))

