import qrcode

# taking upi id as a input
UPI_ID=input("Enter Your UPI ID")

#Defining the payment url based on the upi id and the payment aap

phonepe_url=f"upi://pay?pa={UPI_ID}&pn=Recipient%20NAME&mc=1234"
paytm_url=f"upi://pay?pa={UPI_ID}&pn=Recipient%20NAME&mc=1234"
googlepe_url=f"upi://pay?pa={UPI_ID}&pn=Recipient%20NAME&mc=1234"

#create OQ codes for each payment aap 

phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
googlepe_qr=qrcode.make(googlepe_url)

# save the QR code to image file (option)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("phonepe_qr.png")
googlepe_qr.save("phonepe_qr.png")

# show the QR code
phonepe_qr.show()