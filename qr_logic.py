import qrcode

def generate_my_qr(data, file_name):
    # --- STEP 1: Configure the Generator (Library Logic) ---
    qr = qrcode.QRCode(
        version=1, # Controls the size (1 is smallest)

        #error_correction=qrcode.constants.ERROR_CORRECT_L is used when you dont want a logo in the middle
        error_correction=qrcode.constants.ERROR_CORRECT_H, # About 7% damage recovery
        box_size=10, # How many pixels each "dot" is
        border=4,    # Thickness of the white border
    
    )
    

    # --- STEP 2: Feed the data ---
    qr.add_data(data)
    qr.make(fit=True)

    # --- STEP 3: Create the Image ---
    img = qr.make_image(fill_color="black", back_color="white")

    # --- STEP 4: Save it (Manual Logic) ---
    img.save(file_name)
    print(f"Success! QR code saved as {file_name}")

# --- EXECUTION ---
# This is where you decide WHAT goes into the code
user_input = input("Enter the url you would like to encode: ")
generate_my_qr(user_input, "my_first_qr.png")