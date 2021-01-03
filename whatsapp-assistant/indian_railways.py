#!/usr/bin/env python


### https://paytm.com/train-tickets/pnr-enquiry/4360393388
import requests

def check_pnr(pnr='4360393388'):
    if len(pnr) != 10:
        return "Please enter a valid PNR"
    result = "***START***\n"
    headers = {
        'authority': 'travel.paytm.com',
        'sec-fetch-dest': 'empty',
        'accept': '*/*',
        'origin': 'https://paytm.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://paytm.com/train-tickets/pnr-status',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    params = (
        ('vertical', 'train'),
        ('client', 'web'),
        ('pnr_number', pnr),
        )

    response = requests.get('https://travel.paytm.com/api/trains/v1/status', headers=headers, params=params)
    if response.status_code == 200:
        res = response.json()
        body = res['body']
        # pnr = body['pnr_number']
        # train_name = body['train_name']
        # train_number = body['train_number']
        # quota = body['quota']
        # date = body['date']
        # boarding_details = body['boarding_station'] #dict
        # arrival_details = body['reservation_upto'] #dict
        # chart_prepared = body['chart_prepared'] #bool
        for k, v in body.items():
            if k not in ['boarding_station', 'order_id', 'pax_info', 'pnr_message', 'quota', 'reservation_upto', 'source_station', 'tip_enabled', 'tip_text']:
                result+=f"{k}: {v}\n"
        result += "\nPassenger Info:\n"
        for i in body['pax_info']:
            result += f"{i['passengerName']}\t{i['currentStatus']} {i['currentCoachId']} {i['currentBerthNo']}\n"
        result+="\nDeparture Details:\n"
        for k, v in body['boarding_station'].items():
            result+=f"{k}: {v}\n"
        result+="\nArrival Details:\n"
        for k, v in body['reservation_upto'].items():
            result+=f"{k}: {v}\n"
        result += "***END***"
    else:
        print("Something went wrong")
        return response.text
    return result


