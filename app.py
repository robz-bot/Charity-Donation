from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  
app = Flask(__name__)
CORS(app)  
# Sample dataset
donations = [
    {
        'DonationFrequency': 'One-time',
        'DonationAmount': '1000',
        'DonorName': 'Alice',
        'DonorEmail': 'alice@example.com',
        'PaymentMethod': 'CARD',
        "cardNumber":'XXXX-XXXX-X234',
        "cvv":123,
        "upi":''
    },
    {
        'DonationFrequency': 'Monthly',
        'DonationAmount': '500',
        'DonorName': 'Bob',
        'DonorEmail': 'bob@example.com',
        'PaymentMethod': 'UPI',
         "cardNumber":'',
        "cvv":'',
        "upi":'asd@upi.com'
    },
    {
        'DonationFrequency': 'One-time',
        'DonationAmount': '2000',
        'DonorName': 'Charlie',
        'DonorEmail': 'charlie@example.com',
        'PaymentMethod': 'CARD',
        "cardNumber":'XXXX-XXXX-X202',
        "cvv":'123',
        "upi":''
    },
    {
        'DonationFrequency': 'Monthly',
        'DonationAmount': '7500',
        'DonorName': 'David',
        'DonorEmail': 'david@example.com',
        'PaymentMethod': 'UPI',
         "cardNumber":'',
        "cvv":'',
        "upi":'asd@upi.com'
    },
    {
        'DonationFrequency': 'One-time',
        'DonationAmount': '3000',
        'DonorName': 'Eve',
        'DonorEmail': 'eve@example.com',
        'PaymentMethod': 'CARD',
         "cardNumber":'XXXX-XXXX-X877',
        "cvv":'123',
        "upi":''
    },
    {
        'DonationFrequency': 'Monthly',
        'DonationAmount': '1000',
        'DonorName': 'Frank',
        'DonorEmail': 'frank@example.com',
        'PaymentMethod': 'UPI',
        "cardNumber":'',
        "cvv":'',
        "upi":'asd@upi.com'
    },
    {
        'DonationFrequency': 'One-time',
        'DonationAmount': '4000',
        'DonorName': 'Grace',
        'DonorEmail': 'grace@example.com',
        'PaymentMethod': 'CARD',
        "cardNumber":'XXXX-XXXX-X502',
        "cvv":'123',
        "upi":''
    },
    {
        'DonationFrequency': 'Monthly',
        'DonationAmount': '1250',
        'DonorName': 'Henry',
        'DonorEmail': 'henry@example.com',
        'PaymentMethod': 'UPI',
        "cardNumber":'',
        "cvv":'',
        "upi":'asd@upi.com'
    },
    {
        'DonationFrequency': 'One-time',
        'DonationAmount': '5000',
        'DonorName': 'Ivy',
        'DonorEmail': 'ivy@example.com',
        'PaymentMethod': 'CARD',
        "cardNumber":'XXXX-XXXX-X902',
        "cvv":'123',
        "upi":''
    },
    {
        'DonationFrequency': 'Monthly',
        'DonationAmount': '1500',
        'DonorName': 'Jack',
        'DonorEmail': 'jack@example.com',
        'PaymentMethod': 'UPI',
        "cardNumber":'',
        "cvv":'',
        "upi":'asd@upi.com'
    }
]

@app.route('/submit_donation', methods=['POST'])
def submit_donation():
    try:
        print(request.form)
        # Retrieve form data
        donation_frequency = request.form.get('DonationFrequency')
        donation_amount = request.form.get('flexRadioDefault')
        custom_amount = request.form.get('custom-amount')
        donor_name = request.form.get('donation-name')
        donor_email = request.form.get('donation-email')
        payment_method = request.form.get('DonationPayment')
        cardNumber = request.form.get('cardNumber')
        masked_card_number = mask_card_number(cardNumber)
        cvv = request.form.get('cvv')
        upi = request.form.get('upi')

        # Validate form data (add more validation as needed)
        if not donation_frequency or not donor_name or not donor_email or not payment_method:
            return jsonify({"success": False, "message": "Please fill in all required fields."})

        # Store donation information (replace with database storage)
        donation_info = {
            "DonationFrequency": donation_frequency,
            "DonationAmount": donation_amount if donation_amount != 'custom' else custom_amount,
            "DonorName": donor_name,
            "DonorEmail": donor_email,
            "PaymentMethod": payment_method,
            "cardNumber":masked_card_number,
            "cvv":cvv,
            "upi":upi
        }
        donations.append(donation_info)

        # Return success message
        return jsonify({"success": True, "message": "Thank you for your donation!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"})

def mask_card_number(full_card_number):
    # Mask all but the last three digits
    masked_number = "XXXX-XXXX-X" + full_card_number[-3:]
    return masked_number

@app.route('/get_donations', methods=['GET'])
def get_donations():
    try:
        # Retrieve all donation records
        return jsonify({"success": True, "donations": donations})

    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
