import requests

img="https://img.freepik.com/free-photo/embroidery-art-handicraft_469670-35.jpg?t=st=1731770492~exp=1731774092~hmac=abb84d0051ea4aec835b7af7baf357a746f9203910a7d5dea87f298f9322688a&w=360"
response = requests.get(img)
with open("test.jpg", "wb") as file:
    file.write(response.content)