-- Creating Triggers.
CREATE Triggers qty_decrease
AFTER INSERT ON order_times
FOR EACH ROWS
UPDATE items
SET quantity = quantity - NEW.number
WHERE id = NEW.item_id;
