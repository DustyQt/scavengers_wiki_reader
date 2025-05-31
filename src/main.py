from fandom.api_controller import ApiController

controller = ApiController()
response = controller.create_page('sup', 'this is a chenasasdge in the content')
print(response.content)