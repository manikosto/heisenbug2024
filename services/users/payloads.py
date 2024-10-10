from faker import Faker

faker = Faker()

class Payloads:

    def create_user(self, email=faker.email()):
        return {
          "email": email,
          "password": faker.password(),
          "name": faker.first_name(),
          "nickname": faker.user_name()
        }
