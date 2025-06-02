from fandom.api_controller import ApiController

controller = ApiController()
response = controller.get_page('Mago')
pages = response.json()['query']['pages']
for page_id, page in pages.items():
    content = page['revisions'][0]['*'] if 'revisions' in page else ''
    print(content)
