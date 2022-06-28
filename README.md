# ecommerce_project
Full Fledged E-Commerce website using python, flask and MySql database.


E-commerce Web App
Features/Tasks
1) Users can login
There will be three type of user Admin, Shopuser, and customer in web app, can login via email and password.

2) Users can sign up.
Customer can signup with basic details like DOB, fullname, email, gender, Address. Customers can login the website after email confirmation.

3) Users can reset passwords via reset password via forgot password link received on register email.
User will get password reset link on his register email on clicking the link user will redirect to the web app where they can reset the password

4) Users can update their profile via the settings section.
User have settings on their application where they can update their profile and save it.

5) Users can logout.
Users can log out from the application and redirect on login page.

6) Shop users can register the system and send approval requests to the admin via email.
On the Signup page there is an option for shop registration where shop users can register themselves. After the registration admin gets an approval request for that particular shop user via email.

7) Admin gets email notification and links to Approve/Reject requests.
Whenever the shop user register admin gets the notification on his register email. Once click on the link admin redirect on the application and open request detail page. Admin can either approve or reject. Also reqired reason field for the rejection.

8) Admin can see approval requests.
Admin can see the approval request list page. Click on perticuler request it would open request detail page same as from admin email link.

9) Admin can Create/Update/Delete Shops.
Admin can List/Create/Update/Delete shops from his dashboard. Here admin creating directly so no need to approve/reject request.

10) Once registration requests are accepted then only shop users can login the application.
After request Approval by the Admin Shop user can List/Add/update/delete the product on the webapp. Shop users can Publish/Unpublish products only for their shops.

11) Customers can see the products on landing page.
Only customers can buy the published products. Only Shop users can sell the product.

12) Apply filter and sorting on product page for customers.
Filter the product according to categories, company and filter on the prices, brand, color, material. Sort the product according to price, rating. Search with text. Pagination should be there.

13) customers can add/remove products to their wishlist.
Customer can add the product to their wishlist to see in future. There should be only one wishlist per user.

14) Customers can add products in cart with add/remove functionality from the cart.
There should be a buy now feature/Button also.

15) Create Order from cart by customer.
After clicking on Buy Button then just create order with status paid.

16) Customers can see a list of only their orders.
Create one my orders page there list down all orders. Customers can see details of the order only for their order. Customers can Create/Update orders only for their order. Customers can cancel orders only for their order.

17) Shop users can only see the order for themselves.
Shop users can only see the order for themselves from their dashboard.

18) Shop user Dashboard they can see the percentage of sales of products.
Shop users can see sales of product according to category, brand, for their shops only.cts of shops via dashboard.

19) Admin can see details of the Shops.
Admin can see the list of products under Shops. Admin can see the order of particular Shop and particular customer. Admin can see the details of the product, order, shop user, customer.

20) On the admin user Dashboard they can see the percentage of sales of each shop.
Admin user can see the shop's product sales according to category, brand, shops.

Optional:
Signup/login via social sites.
Global search for Product. categories, company and filter on the prices, brand, color, material. // Optional.
On webapp landing page there will be the global search for the products.

Stripe paymnet integration for buy products.