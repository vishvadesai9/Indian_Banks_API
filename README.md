# Indian_Banks_API
A REST service built using Flask and PostgreSQL that consists of:
  1. Autocomplete API. [/api/branches/autocomplete?q=<branch_name>&limit=<limit>&offset=<offset>]   
    Gets possible matches based on the branch name ordered by
    IFSC code (ascending order) with limit and offset. The input can be a partial branch name and the API will return best possible matches.   
    
Example: https://indianbanksapi.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=2&offset=0  
  Response:  
```
{
  "branches":[
              {
                "address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
                "bank_id":60,
                "branch":"RTGS-HO",
                "city":"MUMBAI",
                "district":"GREATER MUMBAI",
                "ifsc":"ABHY0065001",
                "state":"MAHARASHTRA"
              },
                {"address":"414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
                "bank_id":110,
                "branch":"RTGS-HO",
                "city":"MUMBAI",
                "district":"GREATER BOMBAY",
                "ifsc":"ABNA0000001",
                "state":"MAHARASHTRA"
              }
             ]
}
   ```
     
  

    
    
  2. Search API. [/api/branches/?q=<word>&limit=<limit>&offset=<offset>]    
  Gets possible matches across all columns and all rows, ordered by
    IFSC code (ascending order) with limit and offset. This API searches a term across the database.  
    
 Example: https://indianbanksapi.herokuapp.com/api/branches?q=mumbai&limit=2&offset=0  
  Response:  
```
{
"branches":[
            {
              "address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
              "bank_id":60,
              "branch":"RTGS-HO",
              "city":"MUMBAI",
              "district":"GREATER MUMBAI",
              "ifsc":"ABHY0065001",
              "state":"MAHARASHTRA"
            },
            {
              "address":"ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033",
              "bank_id":60,
              "branch":"ABHYUDAYA NAGAR",
              "city":"MUMBAI",
              "district":"GREATER MUMBAI",
              "ifsc":"ABHY0065002",
              "state":"MAHARASHTRA"
            }
           ]
}
```    
  
  ## Hosting URL
  https://indianbanksapi.herokuapp.com/  
  
  ## Curl Script Example   
  ### Autocomplete API  
  curl -X GET https://indianbanksapi.herokuapp.com/api/branches/autocomplete?q=RTGS"&"limit=3"&"offset=0 -H "Accept: application/json" -H "Content-Type: application/json"     
  
  ### Search API  
  curl -X GET https://indianbanksapi.herokuapp.com/api/branches?q=Bangalore"&"limit=4"&"offset=1 -H "Accept: application/json" -H"Content-Type: application/json"    
  
  
  
  ## Data  
  The PostgreSQL database is hosted on [clever-cloud](https://www.clever-cloud.com/doc/getting-started/quickstart/#create-your-first-add-on)  
  Raw Data: https://github.com/snarayanank2/indian_banks  
  
