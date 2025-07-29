import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/api-sports/api/api-basketball'

mcp = FastMCP('api-basketball')

@mcp.tool()
def timezone() -> dict: 
    '''Get the list of available timezone to be used in the [games] endpoint'''
    url = 'https://api-basketball.p.rapidapi.com/timezone'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def standings(league: Annotated[Union[int, float], Field(description='Fails if field contains anything other than an integer Default: 12')],
              season: Annotated[str, Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')],
              stage: Annotated[Union[str, None], Field(description='')] = None,
              group: Annotated[Union[str, None], Field(description='')] = None,
              team: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None) -> dict: 
    '''Get all available standings | Return a table of one or more rankings according to the league / cup'''
    url = 'https://api-basketball.p.rapidapi.com/standings'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
        'stage': stage,
        'group': group,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def stages(league: Annotated[Union[int, float], Field(description='Fails if field contains anything other than an integer Default: 12')],
           season: Annotated[str, Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')]) -> dict: 
    '''Get all available stages for standings'''
    url = 'https://api-basketball.p.rapidapi.com/standings/stages'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'league': league,
        'season': season,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def groups(season: Annotated[str, Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')],
           league: Annotated[Union[int, float], Field(description='Fails if field contains anything other than an integer Default: 12')]) -> dict: 
    '''Get all available groups for standings'''
    url = 'https://api-basketball.p.rapidapi.com/standings/groups'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def seasons() -> dict: 
    '''Get all available seasons | All {season} can be used in other endpoints as filters'''
    url = 'https://api-basketball.p.rapidapi.com/seasons'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries(name: Annotated[Union[str, None], Field(description='Fails if field contains anything other than alpha-numeric characters, numbers or space')] = None,
              id: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
              code: Annotated[Union[str, None], Field(description='2 characters | Fails if field has anything other than alphabetic characters | Ex : FR, GB, IT...')] = None,
              search: Annotated[Union[str, None], Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')] = None) -> dict: 
    '''Get all available countries | The {country} and {code} keys can be used in other endpoints as filters'''
    url = 'https://api-basketball.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'id': id,
        'code': code,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def leagues(country: Annotated[Union[str, None], Field(description='Fails if field contains anything other than alpha-numeric characters, numbers or space')] = None,
            id: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
            type: Annotated[Union[str, None], Field(description='Fails if field is not within a predetermined list : [league,cup]')] = None,
            season: Annotated[Union[str, None], Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')] = None,
            name: Annotated[Union[str, None], Field(description='Fails if field contains anything other than alpha-numeric characters, numbers or space')] = None,
            code: Annotated[Union[str, None], Field(description='2 characters | Fails if field has anything other than alphabetic characters | Ex : FR, GB, IT...')] = None,
            search: Annotated[Union[str, None], Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')] = None,
            country_id: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None) -> dict: 
    '''Get all available leagues | The league {id} are unique in the API and leagues keep it across all seasons'''
    url = 'https://api-basketball.p.rapidapi.com/leagues'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'id': id,
        'type': type,
        'season': season,
        'name': name,
        'code': code,
        'search': search,
        'country_id': country_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def head2_head(h2h: Annotated[str, Field(description='Fails if field does not match the regular expression : [id-id]')],
               league: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
               season: Annotated[Union[str, None], Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')] = None,
               timezone: Annotated[Union[str, None], Field(description='Fails if field is not a result of the endpoint timezone')] = None) -> dict: 
    '''Get all head to head between two teams'''
    url = 'https://api-basketball.p.rapidapi.com/games'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'h2h': h2h,
        'league': league,
        'season': season,
        'timezone': timezone,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games(timezone: Annotated[Union[str, None], Field(description='Fails if field is not a result of the endpoint timezone')] = None,
          season: Annotated[Union[str, None], Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')] = None,
          id: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
          league: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
          date: Annotated[Union[str, datetime, None], Field(description='Fails if field does not contain a valid date : [YYYY-MM-DD]')] = None,
          team: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None) -> dict: 
    '''Get all available games'''
    url = 'https://api-basketball.p.rapidapi.com/games'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'timezone': timezone,
        'season': season,
        'id': id,
        'league': league,
        'date': date,
        'team': team,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_statistics(season: Annotated[str, Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')],
                     league: Annotated[Union[int, float], Field(description='Fails if field contains anything other than an integer Default: 12')],
                     team: Annotated[Union[int, float], Field(description='Fails if field contains anything other than an integer Default: 133')],
                     date: Annotated[Union[str, datetime, None], Field(description='Fails if field does not contain a valid date : [YYYY-MM-DD]')] = None) -> dict: 
    '''Get team statistics'''
    url = 'https://api-basketball.p.rapidapi.com/statistics'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'season': season,
        'league': league,
        'team': team,
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def teams_informations(name: Annotated[Union[str, None], Field(description='Fails if field contains anything other than alpha-numeric characters, numbers, dashes or space')] = None,
                       league: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 12')] = None,
                       id: Annotated[Union[int, float, None], Field(description='Fails if field contains anything other than an integer Default: 0')] = None,
                       season: Annotated[Union[str, None], Field(description='Fails if field contains anything other than a valid season [YYYY] or [YYYY-YYYY]')] = None,
                       search: Annotated[Union[str, None], Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')] = None) -> dict: 
    '''Get all available teams | The team {id} are unique in the API and teams keep it among all the leagues/cups in which they participate'''
    url = 'https://api-basketball.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'name': name,
        'league': league,
        'id': id,
        'season': season,
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bets(search: Annotated[str, Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')]) -> dict: 
    '''get all available bets labels | All bets {id} can be used in endpoint [odds] as filters'''
    url = 'https://api-basketball.p.rapidapi.com/bets'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_bookmakers(search: Annotated[str, Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')]) -> dict: 
    '''get all available bookmakers | All bookmakers {id} can be used in endpoint [odds] as filters'''
    url = 'https://api-basketball.p.rapidapi.com/bookmakers'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_countries(search: Annotated[str, Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')]) -> dict: 
    '''Get all available countries | The {country} and {code} keys can be used in other endpoints as filters'''
    url = 'https://api-basketball.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_leagues(search: Annotated[str, Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')]) -> dict: 
    '''Get all available leagues | The league {id} are unique in the API and leagues keep it across all seasons'''
    url = 'https://api-basketball.p.rapidapi.com/leagues'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_teams(search: Annotated[str, Field(description='3 characters minimum | Fails if field has anything other than alphabetic characters')]) -> dict: 
    '''Get all available teams | The team {id} are unique in the API and teams keep it among all the leagues/cups in which they participate'''
    url = 'https://api-basketball.p.rapidapi.com/teams'
    headers = {'x-rapidapi-host': 'api-basketball.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search': search,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
