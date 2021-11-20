body = r"""title
Sheffield ⇀ Manchester Piccadilly
Order ID: 16719955573
Issued
Dear customer ,
Your tickets have been issued. Your e-tickets are ready and attached to this email. You can also view them in the app.
You can download free TrainPal App to manage your booking.
[Notice]
16-25 Railcard has been applied. Please bring your Railcard or the device with your digital railcard at all times during the journey in order to qualify for the discount.
Journey information
Sheffield ⇀ Manchester Piccadilly
OUT
Mon 8 Nov 2021
Seat info
08:32
Sheffield
Train
1h 9m
Northern
Any unreserved seat
09:41
Manchester Piccadilly
Ticket Information
Passenger(s)
1 Adult
Railcard(s)
16-25 Railcard x 1
✗ Non-refundable
✓ Exchangeable
Standard Class
Travel is allowed via any permitted route.
Ticket restrictions
Payment details
Transaction id
2138004000381382
Transaction date
TicketPrice
£3.95
Bookingfee
£0.00
Total amount
£3.95
Manage your bookings with the TrainPal App
Contact us
If you have any questions, please view our help& FAQs or contact us via App .
Thank you for choosing TrainPal
Customer Service Department
Travel further for less
Do not forward this mail as it contains your personal information and booking details."""

input_data = {
    "subject": r"Your booking confirmation: Sheffield - Manchester Piccadilly",
    "body": body,
}
