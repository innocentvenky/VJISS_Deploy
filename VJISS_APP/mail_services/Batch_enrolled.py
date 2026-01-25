def batch_enrolled_template(student_name, batch_type, course_name,trainer_name):
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#f4f6f8; font-family:Arial, sans-serif;">

    <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f6f8;padding:20px;">
      <tr>
        <td align="center">
          <table width="100%" cellpadding="0" cellspacing="0"
            style="max-width:600px;background:#ffffff;border-radius:10px;padding:28px;
            box-shadow:0 12px 32px rgba(0,0,0,0.15);">

            <!-- Header -->
            <tr>
              <td align="center">
                <h2 style="margin:0;color:#111827;">
                  🧑‍🏫 Batch Enrollment Successful 🧑‍🏫
                </h2>
              </td>
            </tr>

            <!-- Batch Type -->
            <tr>
              <td align="center" style="padding:16px;">
                <div style="
                  background:#f0fdf4;
                  padding:14px 20px;
                  border-radius:8px;
                  font-weight:bold;
                  color:#166534;
                  box-shadow:0 0 14px rgba(22,101,52,0.35);
                ">
                  Batch Type: {batch_type}
                </div>
              </td>
            </tr>

            <!-- Body -->
            <tr>
              <td style="color:#374151;font-size:15px;line-height:1.6;">
                <p>Hello <strong>{student_name}</strong>,</p>
                <p>🎉 You have successfully enrolled in the selected batch  </p>
                <p> Batch Name   <strong>{course_name}</strong></p>
                <p> Trainer Name   <strong>{trainer_name}</strong>
                <p>⏳ Your batch enrollment is currently under review.</p>
                <p>You will be notified once the batch is approved and scheduled.</p>
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
                  <span style="font-size:13px;">
                    This is an automated message, please do not reply.
                  </span>
                </p>
              </td>
            </tr>

          </table>
        </td>
      </tr>
    </table>

    </body>
    </html>
    """