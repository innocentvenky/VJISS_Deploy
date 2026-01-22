from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from rest_framework import status
from VJISS_APP.models import Create_User
from django.core.cache import cache
class SendOtp(APIView):
    def generate_otp(self, length=6):
        return "".join(str(random.randint(0, 9)) for _ in range(length))

    def post(self, request):
        email = request.data.get('email')
        user=Create_User.objects.filter(email=email).exists()
        print(user)
        print(email , not user)
        
        if not email:
            

            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        otp = self.generate_otp()
          # 🔐 store OTP in cache (5 minutes)
        cache_key = f"otp_{email}"
        cache.set(cache_key, otp, timeout=300)

        subject = "🔐 OTP Verification Code"
        message =  f"""
    <html>
    <body style="font-family: Arial, sans-serif;">

        <h2>OTP Verification</h2>

        <p>Your verification code is:</p>

        <div style="
            font-size: 40px;
            font-weight: bold;
            letter-spacing: 8px;
            color: #1e90ff;
            background-color: #f0f6ff;
            padding: 18px 28px;
            border-radius: 8px;
            display: inline-block;
        ">
            {otp}
        </div>

        <p style="margin-top: 20px;">
            This OTP is valid for <b>5 minutes</b>.
            Do not share this OTP with anyone.
        </p>

        <p>If this request was not made by you, please ignore this email.</p>

        <p>Regards,<br><b>Support Team</b></p>

    </body>
    </html>
    """

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,

                [email],
                fail_silently=False,
        html_message=message
            )
            return Response(
                {"message": "OTP sent successfully"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

