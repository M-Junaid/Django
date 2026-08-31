
from rest_framework.test import APITestCase, APIClient
# APITestCase -> Test API requests automatically
class StudentAPITest(APITestCase):
    # setUp() --> "prepare the API client"
    #Before each test, prepare an API client. 
    def setUp(self):
        # APIClient gives your test a way to act like a client making API requests.
        self.client = APIClient()

    def test_unauthenticated_user_cannot_access_student_list(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 401) 