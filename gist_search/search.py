from gist_search.utils import get_gists


def search_gists(username, description=None, file_name=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    gists = get_gists(username)
    
    result=[]
    
    for gist in gists:
        #first condition description
        if description and description.lower() not in gist['description'].lower():
            continue
        
        #second condition file_name
        if file_name:
            matched=False
            for key, values in gist['files'].items():
                if file_name.lower() in key.lower():
                    matched=True
            if not matched:
                continue
            
        result.append(gist)
        
    return result
    
