from flask import Flask, request 
from googlesearch import search 
from twilio.twiml.messaging_response import MessagingResponse   

app = Flask(__name__) 

@app.route("/sms", methods=['POST']) 
def bot(): 
    user_msg = request.vaules.get('Body', '').lower()
    response = MessagingResponse() 
    q = user_msg + " espn.com " 
    result = [url for url in search(q, num_results=3)]  
    msg = response.message(f"-----results for {user_msg}-----\n") 

    for res in result: 
        msg.body(res + "\n") 
    return str(response) 

if __name__ == "__main__": 
    app.run() 