import qrcode
from PIL import Image # You need this for the "image surgery"

def generate_my_qr_with_logo(data, file_name, logo_path):
    # --- STEP 1: Configure (High Error Correction is mandatory for logos) ---
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H, 
        box_size=10,
        border=4,
    )
    
    # --- STEP 2: Feed the data ---
    qr.add_data(data)
    qr.make(fit=True)

    # --- STEP 3: Create the QR Image ---
    # We convert to 'RGB' so we can paste a colored logo onto it
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # --- STEP 4: The Logo "Manual Logic" ---
    try:
        logo = Image.open("/Users/william/Downloads/PNGFormat Original.png")
        
        # Calculate how big the logo should be (20% of QR code size is safe)
        qr_width, qr_height = qr_img.size
        logo_max_size = qr_width // 5 
        logo = logo.resize((logo_max_size, logo_max_size))

        # Calculate the center position (Math logic: (Total - Part) / 2)
        logo_pos = (
            (qr_width - logo_max_size) // 2, 
            (qr_height - logo_max_size) // 2
        )

        # Paste the logo onto the QR image
        qr_img.paste(logo, logo_pos)
        
    except FileNotFoundError:
        print("Logo file not found. Generating plain QR instead.")

    # --- STEP 5: Save it ---
    qr_img.save(file_name)
    print(f"Success! Branded QR saved as {file_name}")

# --- EXECUTION ---
user_input = input("Enter the url you would like to encode: ")
# Make sure "logo.png" actually exists in your folder!
generate_my_qr_with_logo(user_input, "branded_qr.png", "logo.png")