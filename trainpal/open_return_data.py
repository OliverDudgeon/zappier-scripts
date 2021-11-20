body = r"""title
Oxford ⇋ Sheffield
Order ID: 16837123844
Issued
Dear customer ,
Your tickets have been issued. Your e-tickets are ready and attached to this email. You can also view them in the app.
You can download free TrainPal App to manage your booking.
[Notice]
16-25 Railcard has been applied. Please bring your Railcard or the device with your digital railcard at all times during the journey in order to qualify for the discount.
Journey information
Oxford ⇋ Sheffield
OUT
Mon 22 Nov 2021
Seat info
12:39
Oxford
Train
35m
CrossCountry
Any unreserved seat
13:14
Leamington Spa
Short Change
Change at same station
13:15
Leamington Spa
Train
34m
CrossCountry
Any unreserved seat
13:49
Birmingham New Street
14m
Change at same station
14:03
Birmingham New Street
Train
1h 15m
CrossCountry
Any unreserved seat
15:18
Sheffield
RTN
Open return
Sheffield
Return within 1 month
Valid until Tue 21 Dec 2021
Leamington Spa
Leamington Spa
Return within 1 month
Valid until Tue 21 Dec 2021
Oxford
Ticket Information
Passenger(s)
1 Adult
Railcard(s)
16-25 Railcard x 1
Split tickets
Oxford ⇋ Leamington Spa
Off-Peak Return
✓ Refundable
✗ Non-exchangeable
Standard Class
OUT:
Travel is allowed via any permitted route.
RTN:
Travel is allowed via any permitted route.
Ticket restrictions
Leamington Spa ⇋ Sheffield
Off-Peak Return
✓ Refundable
✗ Non-exchangeable
Standard Class
OUT:
Travel is allowed via any permitted route.
RTN:
Travel is allowed via any permitted route.
Ticket restrictions
Payment details
Transaction id
2149004000202525
Transaction date
19/11/2021
Card type
MASTERCARD
Card number
**** **** **** 2379
TicketPrice
£50.45
Bookingfee
£0.00
VoucherDiscount
-£3.00
Total amount
£47.45
Manage your bookings with the TrainPal App
Contact us
If you have any questions, please view our help& FAQs or contact us via App .
Thank you for choosing TrainPal
Customer Service Department
Travel further for less
Do not forward this mail as it contains your personal information and booking details."""

input_data = {
    "subject": r"Your booking confirmation: Oxford - Sheffield",
    "body": body,
}
