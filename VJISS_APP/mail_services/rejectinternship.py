def reject_internship_template(student_name,internship_title,application_id,applied_on):
    return f'''

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Internship Application Update</title>
  </head>

  <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

    <table width="100%" cellpadding="0" cellspacing="0" style="padding:20px;">
      <tr>
        <td align="center">

          <table width="100%" cellpadding="0" cellspacing="0"
            style="
              max-width:600px;
              background:#ffffff;
              border-radius:10px;
              padding:28px;
              box-shadow:0 12px 32px rgba(0,0,0,0.12);
            ">

            <!-- Header -->
            <tr>
              <td align="center" style="padding-bottom:16px;">
                <h2 style="margin:0; color:#111827;">
                  Internship Application Update
                </h2>
              </td>
            </tr>

            <!-- Message -->
            <tr>
              <td style="color:#374151; font-size:15px; line-height:1.6;">
                <p>Hello <strong>{student_name}</strong>,</p>

                <p>
                  Thank you for taking the time to apply for the internship:
                </p>

                <p style="font-weight:bold; color:#dc2626;">
                  {internship_title}
                </p>

                <p>
                  After careful consideration, we regret to inform you that
                  you have not been selected for this opportunity at this time.
                </p>

                <p>
                  We received many strong applications, and this decision was not easy.
                  We truly appreciate your interest in <strong>VJISS</strong>.
                </p>
              </td>
            </tr>

            <!-- Records -->
            <tr>
              <td style="padding-top:18px;">
                <table width="100%" cellpadding="0" cellspacing="0"
                  style="background:#f9fafb; border-radius:8px; padding:16px;">
                  <tr>
                    <td style="font-size:14px; color:#111827;">
                      <strong>Application Details</strong>
                    </td>
                  </tr>
                  <tr>
                    <td style="font-size:14px; color:#374151; padding-top:8px;">
                      Application ID: <strong>{application_id}</strong><br />
                      Applied On: <strong>{applied_on}</strong>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- Encouragement -->
            <tr>
              <td style="padding-top:18px; color:#374151; font-size:15px;">
                <p>
                  We encourage you to apply again in the future as new opportunities arise.
                  We wish you every success in your career journey.
                </p>
              </td>
            </tr>

            <!-- Footer -->
            <tr>
              <td style="padding-top:22px; font-size:14px; color:#6b7280;">
                <p>
                  Kind regards,<br />
                  <strong>VJISS Team</strong><br />
                  +91 8985744204<br />
                  +91 9505557191<br />
                  <span style="font-size:13px;">This is an automated message. Please do not reply.</span>
                </p>
              </td>
            </tr>

          </table>

        </td>
      </tr>
    </table>

  </body>
</html>



'''