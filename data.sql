
-- Insert branches into the `branches` table
-- INSERT INTO branches (id, created_at, branch_name, location, attendant, capacity)
-- VALUES
--     ('1', '2025-01-22 12:00:00', 'Eldoret', 'Downtown', '1', 200),
--     ('2', '2025-01-22 12:05:00', 'Nairobi', 'North Side', '2', 150),
--     ('3', '2025-01-22 12:10:00', 'Kisumu', 'East End', '3', 100), -- No attendant assigned yet
--     ('4', '2025-01-22 12:15:00', 'Mombasa', 'West Park', '4', 180);


-- Insert products into the `products` table
-- INSERT INTO products (id, created_at, name, description, product_type, brand, size, unit_price)
-- VALUES
--     ('1', '2025-01-22 12:30:00', 'K-Gas 6kg', '6kg K-Gas cylinder', 'Gas Cylinder', 'K-Gas', 6.0, 3500.0),
--     ('2', '2025-01-22 12:35:00', 'K-Gas 13kg', '13kg K-Gas cylinder', 'Gas Cylinder', 'K-Gas', 13.0, 6500.0),
--     ('3', '2025-01-22 12:40:00', 'Pro-Gas 6kg', '6kg Pro-Gas cylinder', 'Gas Cylinder', 'Pro-Gas', 6.0, 3200.0),
--     ('4', '2025-01-22 12:45:00', 'Pro-Gas 13kg', '13kg Pro-Gas cylinder', 'Gas Cylinder', 'Pro-Gas', 13.0, 6000.0),
--     ('5', '2025-01-22 12:50:00', 'Gas Burner', 'Standard gas burner', 'Burner', NULL, NULL, 1200.0),
--     ('6', '2025-01-22 12:55:00', 'Cooker', '4-burner gas cooker', 'Appliance', NULL, NULL, 25000.0),
--     ('7', '2025-01-22 13:00:00', 'Pressure Regulator', 'Gas pressure regulator for cylinders', 'Regulator', NULL, NULL, 800.0);


-- Insert inventory records into the `inventory` table
-- INSERT INTO inventory (id, created_at, product_id, branch_id, quantity, last_updated)
-- VALUES
--     -- Eldoret (Branch ID 1)
--     ('1', '2025-01-22 13:05:00', '1', '1', 50, '2025-01-22'),
--     ('2', '2025-01-22 13:10:00', '2', '1', 30, '2025-01-22'),
--     ('3', '2025-01-22 13:15:00', '3', '1', 40, '2025-01-22'),
--     ('4', '2025-01-22 13:20:00', '4', '1', 20, '2025-01-22'),
--     ('5', '2025-01-22 13:25:00', '5', '1', 60, '2025-01-22'),
--     ('6', '2025-01-22 13:30:00', '6', '1', 10, '2025-01-22'),
--     ('7', '2025-01-22 13:35:00', '7', '1', 80, '2025-01-22'),

--     -- Nairobi (Branch ID 2)
--     ('8', '2025-01-23 13:40:00', '1', '2', 60, '2025-01-23'),
--     ('9', '2025-01-23 13:45:00', '2', '2', 40, '2025-01-23'),
--     ('10', '2025-01-23 13:50:00', '3', '2', 50, '2025-01-23'),
--     ('11', '2025-01-23 13:55:00', '4', '2', 25, '2025-01-23'),
--     ('12', '2025-01-23 14:00:00', '5', '2', 70, '2025-01-23'),
--     ('13', '2025-01-23 14:05:00', '6', '2', 15, '2025-01-23'),
--     ('14', '2025-01-23 14:10:00', '7', '2', 90, '2025-01-23'),

--     -- Kisumu (Branch ID 3)
--     ('15', '2025-01-24 14:15:00', '1', '3', 30, '2025-01-24'),
--     ('16', '2025-01-24 14:20:00', '2', '3', 20, '2025-01-24'),
--     ('17', '2025-01-24 14:25:00', '3', '3', 25, '2025-01-24'),
--     ('18', '2025-01-24 14:30:00', '4', '3', 10, '2025-01-24'),
--     ('19', '2025-01-24 14:35:00', '5', '3', 40, '2025-01-24'),
--     ('20', '2025-01-24 14:40:00', '6', '3', 5, '2025-01-24'),
--     ('21', '2025-01-24 14:45:00', '7', '3', 50, '2025-01-24'),

--     -- Mombasa (Branch ID 4)
--     ('22', '2025-01-25 14:50:00', '1', '4', 40, '2025-01-25'),
--     ('23', '2025-01-25 14:55:00', '2', '4', 30, '2025-01-25'),
--     ('24', '2025-01-25 15:00:00', '3', '4', 35, '2025-01-25'),
--     ('25', '2025-01-25 15:05:00', '4', '4', 15, '2025-01-25'),
--     ('26', '2025-01-25 15:10:00', '5', '4', 50, '2025-01-25'),
--     ('27', '2025-01-25 15:15:00', '6', '4', 8, '2025-01-25'),
--     ('28', '2025-01-25 15:20:00', '7', '4', 60, '2025-01-25');


-- Insert customers into the `customers` table
-- INSERT INTO customers (id, created_at, name, phone, email, address, account_balance)
-- VALUES
--     ('1', '2025-01-27 15:30:00', 'John Doe', '0721234567', 'john.doe@example.com', '123 Downtown Street, Eldoret', 500.00),
--     ('2', '2025-01-27 15:35:00', 'Jane Smith', '0729876543', 'jane.smith@example.com', '45 Upper Hill Road, Nairobi', 1200.00),
--     ('3', '2025-01-27 15:40:00', 'Alice Johnson', '0734567890', NULL, '789 Coastal Lane, Mombasa', 300.00),
--     ('4', '2025-01-27 15:45:00', 'Bob Brown', '0712345678', 'bob.brown@example.com', NULL, 750.00),
--     ('5', '2025-01-27 15:50:00', 'Eve White', '0725678901', 'eve.white@example.com', '56 East End, Kisumu', 1000.00);


-- Insert suppliers into the `suppliers` table
-- INSERT INTO suppliers (id, created_at, name, contact_person, phone, email, address, account_balance)
-- VALUES
--     ('1', '2025-01-27 16:00:00', 'GasCo Ltd', 'James Mwangi', '0723456789', 'james.mwangi@gasco.com', '123 Industrial Area, Nairobi', 50000.00),
--     ('2', '2025-01-27 16:05:00', 'Flame Distributors', 'Lucy Wanjiru', '0712345678', 'lucy.wanjiru@flamedist.com', '456 Warehouse Lane, Mombasa', 35000.00),
--     ('3', '2025-01-27 16:10:00', 'Cookware Supplies', 'Peter Otieno', '0734567890', NULL, '789 Traders Avenue, Kisumu', 20000.00),
--     ('4', '2025-01-27 16:15:00', 'KitchenPro', 'Diana Nyaga', '0725678901', 'diana.nyaga@kitchenpro.com', '321 Downtown Road, Nakuru', 10000.00),
--     ('5', '2025-01-27 16:20:00', 'GasTech Solutions', 'John Kariuki', '0745678902', 'john.kariuki@gastech.com', '567 Highlands Street, Eldoret', 45000.00);


-- Insert new products into the `products` table
-- INSERT INTO products (id, created_at, name, description, product_type, brand, size, unit_price)
-- VALUES
--     ('8', '2025-01-27 17:00:00', 'K-Gas-Empty 6kg', 'Empty 6kg gas cylinder', 'gas-cylinder', 'K-Gas', 6, 1500.00),
--     ('9', '2025-01-27 17:05:00', 'K-Gas-Empty 13kg', 'Empty 13kg gas cylinder', 'gas-cylinder', 'K-Gas', 13, 2500.00),
--     ('10', '2025-01-27 17:10:00', 'Pro-Gas-Empty 6kg', 'Empty 6kg gas cylinder', 'gas-cylinder', 'Pro-Gas', 6, 1400.00),
--     ('11', '2025-01-27 17:15:00', 'Pro-Gas-Empty 13kg', 'Empty 13kg gas cylinder', 'gas-cylinder', 'Pro-Gas', 13, 2300.00);


-- Insert inventory for the new products into the `inventory` table
-- INSERT INTO inventory (id, created_at, product_id, branch_id, quantity, last_updated)
-- VALUES
--     ('29', '2025-01-27 17:20:00', '8', '1', 20, '2025-01-27'),
--     ('30', '2025-01-27 17:25:00', '11', '1', 15, '2025-01-27'),
--     ('31', '2025-01-27 17:30:00', '9', '2', 25, '2025-01-27'),
--     ('32', '2025-01-27 17:35:00', '10', '2', 20, '2025-01-27'),
--     ('33', '2025-01-27 17:40:00', '9', '3', 10, '2025-01-27'),
--     ('34', '2025-01-27 17:45:00', '11', '3', 8, '2025-01-27'),
--     ('35', '2025-01-27 17:50:00', '8', '4', 18, '2025-01-27'),
--     ('36', '2025-01-27 17:55:00', '9', '4', 12, '2025-01-27');

-- Insert sales into the `sales` table
-- INSERT INTO sales (id, created_at, branch_id, customer_id, sale_date, total_amount, payment_method, status)
-- VALUES
--     ('1', '2025-01-27 18:00:00', '1', '1', '2025-01-27', 3500.00, 'cash', 'completed'),
--     ('2', '2025-01-27 18:10:00', '2', '2', '2025-01-27', 4400.00, 'mpesa', 'completed'),
--     ('3', '2025-01-27 18:20:00', '3', NULL, '2025-01-27', 4500.00, 'credit', 'pending'),
--     ('4', '2025-01-27 18:30:00', '4', '3', '2025-01-27', 4300.00, 'cash', 'completed');

-- -- Insert sale items into the `sale_items` table
-- INSERT INTO sale_items (id, created_at, sale_id, product_id, quantity, price_per_unit)
-- VALUES
--     -- Sale 1 (Eldoret branch)
--     ('1', '2025-01-27 18:01:00', '1', '1', 2, 2000.00), -- 2 units of K-Gas 6kg
--     ('2', '2025-01-27 18:02:00', '1', '3', 1, 1500.00), -- 

--     -- Sale 2 (Nairobi branch)
--     ('3', '2025-01-27 18:11:00', '2', '2', 1, 3000.00), -- 1 unit of K-Gas 13kg
--     ('4', '2025-01-27 18:12:00', '2', '4', 3, 1400.00), -- 

--     -- Sale 3 (Kisumu branch, customer unknown)
--     ('5', '2025-01-27 18:21:00', '3', '3', 1, 4500.00), -- 1 unit of gas burner

--     -- Sale 4 (Mombasa branch)
--     ('6', '2025-01-27 18:31:00', '4', '5', 2, 2000.00), -- 2 units of K-Gas 6kg
--     ('7', '2025-01-27 18:32:00', '4', '2', 1, 2300.00); -- 


-- Insert an invoice for Sale 3
-- INSERT INTO invoices (id, created_at, sale_id, invoice_date, due_date, total_amount, paid_amount, balance_due)
-- VALUES
--     ('1', '2025-01-27 18:25:00', '3', '2025-01-27', '2025-02-27', 4500.00, 0.00, 4500.00);


-- Insert additional credit sales into the `sales` table
-- INSERT INTO sales (id, created_at, branch_id, customer_id, sale_date, total_amount, payment_method, status)
-- VALUES
--     ('5', '2025-01-27 19:00:00', '1', '5', '2025-01-27', 3500.00, 'credit', 'pending'),
--     ('6', '2025-01-27 19:30:00', '2', '4', '2025-01-27', 7200.00, 'credit', 'pending'),
--     ('7', '2025-01-27 20:00:00', '3', '3', '2025-01-27', 1500.00, 'credit', 'pending');

-- -- Insert sale items for Sale ID 4
-- INSERT INTO sale_items (id, created_at, sale_id, product_id, quantity, price_per_unit)
-- VALUES
--     ('8', '2025-01-27 19:10:00', '5', '1', 2, 1000.00), -- K-Gas 6kg x 2
--     ('9', '2025-01-27 19:12:00', '5', '3', 1, 1500.00); -- Gas Burner x 1

-- -- Insert sale items for Sale ID 5
-- INSERT INTO sale_items (id, created_at, sale_id, product_id, quantity, price_per_unit)
-- VALUES
--     ('10', '2025-01-27 19:40:00', '6', '2', 3, 1200.00), -- Pro-Gas 6kg x 3
--     ('11', '2025-01-27 19:42:00', '6', '5', 2, 1800.00); -- Cooker x 2

-- Insert sale items for Sale ID 6
-- INSERT INTO sale_items (id, created_at, sale_id, product_id, quantity, price_per_unit)
-- VALUES
--     ('12', '2025-01-27 20:10:00', '7', '1', 1, 1000.00) -- K-Gas 6kg x 1


-- Insert invoices for the additional credit sales into the `invoices` table
-- INSERT INTO invoices (id, created_at, sale_id, invoice_date, due_date, total_amount, paid_amount, balance_due)
-- VALUES
--     ('2', '2025-01-27 19:05:00', '5', '2025-01-27', '2025-02-27', 3500.00, 0.00, 3500.00),
--     ('3', '2025-01-27 19:35:00', '6', '2025-01-27', '2025-02-27', 7200.00, 0.00, 7200.00),
--     ('4', '2025-01-27 20:05:00', '7', '2025-01-27', '2025-02-27', 1500.00, 0.00, 1500.00);

-- Receipt for Invoice ID 1 (Sale ID 4)
-- INSERT INTO receipts (id, created_at, invoice_id, receipt_date, amount_received, receipt_method)
-- VALUES
--     ('1', '2025-01-27 21:00:00', '1', '2025-01-27', 4500.00, 'cash'),
--     ('2', '2025-01-27 21:30:00', '2', '2025-01-27', 2000.00, 'mpesa'),
--     ('3', '2025-01-27 22:15:00', '3', '2025-01-27', 1000.00, 'cash'); -- Partial payment

-- Purchase Invoices
-- INSERT INTO purchase_invoices (id, created_at, supplier_id, invoice_date, total_amount, paid_amount, balance_due, status)
-- VALUES
--     ('1', '2025-01-27 12:00:00', '1', '2025-01-25', 13500.00, 7000.00, 6500.00, 'pending'),
--     ('2', '2025-01-27 12:10:00', '2', '2025-01-26', 18000.00, 18000.00, 0.00, 'completed'),
--     ('3', '2025-01-27 12:20:00', '3', '2025-01-26', 22000.00, 10000.00, 12000.00, 'pending');

-- Items for Purchase Invoice ID 1
-- INSERT INTO purchase_invoice_items (id, created_at, purchase_invoice_id, product_id, quantity, unit_price, total_price)
-- VALUES
--     ('1', '2025-01-27 12:30:00', '1', '1', 30, 150.00, 4500.00),
--     ('2', '2025-01-27 12:35:00', '1', '2', 20, 200.00, 4000.00),
--     ('3', '2025-01-27 12:40:00', '1', '3', 20, 250.00, 5000.00);

-- -- Items for Purchase Invoice ID 2
-- INSERT INTO purchase_invoice_items (id, created_at, purchase_invoice_id, product_id, quantity, unit_price, total_price)
-- VALUES
--     ('4', '2025-01-27 12:50:00', '2', '4', 25, 300.00, 7500.00),
--     ('5', '2025-01-27 12:55:00', '2', '5', 50, 210.00, 10500.00);

-- -- Items for Purchase Invoice ID 3
-- INSERT INTO purchase_invoice_items (id, created_at, purchase_invoice_id, product_id, quantity, unit_price, total_price)
-- VALUES
--     ('6', '2025-01-27 13:00:00', '3', '6', 30, 500.00, 15000.00),
--     ('7', '2025-01-27 13:05:00', '3', '7', 20, 350.00, 7000.00);


-- Payments for Supplier ID 1
-- INSERT INTO supplier_payments (id, created_at, supplier_id, purchase_invoice_id, payment_date, amount, payment_method)
-- VALUES
--     ('1', '2025-01-27 14:00:00', '1', '1', '2025-01-27', 3000.00, 'mpesa'),
--     ('2', '2025-01-27 14:10:00', '1', '1', '2025-01-28', 2000.00, 'cash');

-- -- Payments for Supplier ID 2
-- INSERT INTO supplier_payments (id, created_at, supplier_id, purchase_invoice_id, payment_date, amount, payment_method)
-- VALUES
--     ('3', '2025-01-27 14:20:00', '2', '2', '2025-01-27', 18000.00, 'bank'); -- Full payment

-- -- Payments for Supplier ID 3
-- INSERT INTO supplier_payments (id, created_at, supplier_id, purchase_invoice_id, payment_date, amount, payment_method)
-- VALUES
--     ('4', '2025-01-27 14:30:00', '3', '3', '2025-01-27', 5000.00, 'cash'),
--     ('5', '2025-01-27 14:40:00', '3', '3', '2025-01-28', 3500.00, 'mpesa');


-- Insert branch transfers
-- INSERT INTO branch_transfers (id, created_at, from_branch_id, to_branch_id, transfer_date, status, approved_by)
-- VALUES
--     ('1', '2025-01-27 10:00:00', '1', '2', '2025-01-27', 'approved', '1'),
--     ('2', '2025-01-27 11:00:00', '2', '3', '2025-01-27', 'pending', NULL),
--     ('3', '2025-01-27 12:00:00', '3', '1', '2025-01-27', 'approved', '2');


-- -- Insert branch transfer items for transfer ID 1
-- INSERT INTO branch_transfer_items (id, created_at, transfer_id, product_id, quantity)
-- VALUES
--     ('1', '2025-01-27 10:10:00', '1', '1', 50),  -- 50 K-Gas-Empty 6kg
--     ('2', '2025-01-27 10:15:00', '1', '2', 30); -- 30 K-Gas-Empty 13kg

-- -- Insert branch transfer items for transfer ID 2
-- INSERT INTO branch_transfer_items (id, created_at, transfer_id, product_id, quantity)
-- VALUES
--     ('3', '2025-01-27 11:10:00', '2', '4', 40),  -- 40 Pro-Gas-Empty 6kg
--     ('4', '2025-01-27 11:15:00', '2', '5', 20); -- 20 Pro-Gas-Empty 13kg

-- -- Insert branch transfer items for transfer ID 3
-- INSERT INTO branch_transfer_items (id, created_at, transfer_id, product_id, quantity)
-- VALUES
--     ('5', '2025-01-27 12:10:00', '3', '3', 15),  -- 15 K-Gas-Empty 13kg
--     ('6', '2025-01-27 12:15:00', '3', '1', 25); -- 25 K-Gas-Empty 6kg


