from evelink import eve, api
if __name__ == '__main__':
    #eve_api = api.API()
    #response = eve_api.get('/corp/CorporationSheet', {'corporationID': '98143274'})
    #print response.result.find('allianceID').text
    eve_obj = eve.EVE()
    response = eve_obj.affiliations_for_character(90610935)
    print response