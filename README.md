---

# Supply Chain Management System

## Overview
This system is designed to ensure the authenticity and track the movement of fertilizer packages from manufacturers to suppliers, retailers, and farmers. It provides a seamless way to monitor the supply chain, using QR codes for tracking and verifying product information at each checkpoint.

## Features
- **Role-Based Access:** Different roles (manufacturer, wholesaler, retailer, farmer) with specific functionalities.
- **Product Tracking:** Track the movement of fertilizer packages through the supply chain.
- **QR Code Integration:** Use QR codes to provide detailed product information and verify authenticity.
- **Order Management:** View and order available fertilizers up the supply chain.
- **Verification:** Verify products upon arrival for authenticity.

## Tech Stack
- **Backend:** Python Flask
- **Database:** MySQL (for local development)
- **Frontend:** HTML/CSS (using Tailwind CSS from CDN)

## Prerequisites
- **Python:** Ensure you have Python installed. You can download it from [here](https://www.python.org/).
- **Virtualenv:** It's recommended to use virtual environments for Python projects. You can install it using `pip install virtualenv`.

## Setup

### Backend (Flask)
1. **Clone the repository:**
    ```bash
    git clone https://github.com/kc-allan/supply-chain-management-system.git
    cd supply-chain-management-system
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the backend server:**
    ```bash
    flask run
    ```
    The backend server will start on `http://127.0.0.1:5000`.

### Frontend
1. **Navigate to the frontend directory (if applicable):**
    - If you have a separate frontend directory, navigate to it. If the frontend files are integrated with Flask templates, skip this step.

2. **Ensure Tailwind CSS is included in your HTML files:**
    ```html
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    ```

## Running the Project Locally
1. **Start the backend server (Flask):** Follow the instructions in the Backend section above.
2. **Access the application:** Open your web browser and go to `http://localhost:5000`.

## Key Functionalities

### Role-Based Access
- **Manufacturer:** Can add product details, generate QR codes, and track shipments to wholesalers.
- **Wholesaler:** Can view products from manufacturers, place orders, and track shipments to retailers.
- **Retailer:** Can view products from wholesalers, place orders, and track shipments to farmers.
- **Farmer:** Can view and verify product authenticity, place orders from retailers.

### Product Tracking
- **Add Product:** Manufacturers can add new fertilizer products to the system.
- **Generate QR Codes:** QR codes are generated for each product batch to ensure traceability.
- **Track Shipments:** Each checkpoint (manufacturer, wholesaler, retailer, farmer) can update the status of the shipments.

### Order Management
- **View Products:** Users can view available products from one level up in the supply chain.
- **Place Orders:** Users can place orders for products and track their status.

### Verification
- **Scan QR Codes:** Users can scan QR codes to view detailed product information and verify authenticity.
- **Verify Shipments:** Products are verified upon arrival at each checkpoint to ensure they are authentic and tamper-free.

## Contributing
1. **Fork the repository:**
    - Click on the "Fork" button at the top right corner of the repository page.

2. **Clone your fork:**
    ```bash
    git clone https://github.com/yourusername/supply-chain-management-system.git
    cd supply-chain-management-system
    ```

3. **Create a branch for your feature:**
    ```bash
    git checkout -b feature-name
    ```

4. **Make your changes and commit them:**
    ```bash
    git commit -m "Description of the feature or fix"
    ```

5. **Push your changes to your fork:**
    ```bash
    git push origin feature-name
    ```

6. **Create a pull request:**
    - Go to the original repository and click on the "New pull request" button.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions or need further assistance, feel free to contact us at [your-email@example.com](mailto:your-email@example.com).

---

This README provides a comprehensive guide to setting up and running the supply chain management system locally, as well as contributing to its development.
