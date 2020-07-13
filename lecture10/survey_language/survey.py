class AnonymousSurvey(object):
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题，并未存出答案作准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_result(self):
        """显示收集到的所有答卷"""
        print("Survey result:")
        for response in self.responses:
            print('-' + response)
