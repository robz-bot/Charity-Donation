from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  
app = Flask(__name__)
CORS(app)  
# Sample storage for donations (replace with a database in a real-world scenario)
donations = [{
    'DonationFrequency':'One-time', 
    'DonationAmount': '1000', 
    'DonorName':'Mary', 
    'DonorEmail': 'mary@mail.com',
    'PaymentMethod': 'UPI'
}]

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

        # Validate form data (add more validation as needed)
        if not donation_frequency or not donor_name or not donor_email or not payment_method:
            return jsonify({"success": False, "message": "Please fill in all required fields."})

        # Store donation information (replace with database storage)
        donation_info = {
            "DonationFrequency": donation_frequency,
            "DonationAmount": donation_amount if donation_amount != 'custom' else custom_amount,
            "DonorName": donor_name,
            "DonorEmail": donor_email,
            "PaymentMethod": payment_method
        }
        donations.append(donation_info)

        # Return success message
        return jsonify({"success": True, "message": "Thank you for your donation!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"})

@app.route('/get_donations', methods=['GET'])
def get_donations():
    try:
        # Retrieve all donation records
        return jsonify({"success": True, "donations": donations})

    except Exception as e:
        return jsonify({"success": False, "message": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
