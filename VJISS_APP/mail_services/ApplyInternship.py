def internship_applied_template(student_name, internship_title):
    return f"""
    <html>
    <body>
       <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

   <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f8;padding:20px;">
  <tr>
    <td align="center">
      <table width="100%" cellpadding="0" cellspacing="0"
        style="max-width:600px;background:#ffffff;border-radius:10px;padding:28px;
        box-shadow:0 12px 32px rgba(0,0,0,0.15);">

        <tr>
          <td align="center">
            <h2 style="margin:0;color:#111827;">
              🎉 Internship Application Successful 🎉
            </h2>
          </td>
        </tr>

        <tr>
          <td align="center" style="padding:16px;">
            <div style="
              background:#eef2ff;
              padding:14px 20px;
              border-radius:8px;
              font-weight:bold;
              color:#2563eb;
              box-shadow:0 0 14px rgba(37,99,235,0.35);
            ">
              {internship_title}
            </div>
          </td>
        </tr>

        <tr>
          <td style="color:#374151;font-size:15px;line-height:1.6;">
            <p>Hello <strong>{student_name}</strong>,</p>
            <p>You have successfully applied for this internship.</p>
            <p> ⏳ your application under reviewing  </p>
            <p>Our team will contact you soon.</p>
          </td>
        </tr>

          <!-- Footer -->
            <tr>
              <td style="padding-top:24px; font-size:14px; color:#6b7280;">
                <p>
                  Best regards,<br />
                  <strong>VJISS Team</strong><br />
                  +91 8985744204<br />
                  +91 9505557191<br />
                  <span style="font-size:13px;">This is an automated message, please do not reply.</span>
                </p>
              </td>
            </tr>

      </table>
    </td>
  </tr>
</table>


    <!-- Safe animation (ignored gracefully where unsupported) -->
   
    </body>
    </html>
    """
