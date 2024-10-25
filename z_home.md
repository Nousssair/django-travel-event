{% extends "base.html" %}

{% block content %}
<!-- home.html -->
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Accueil - Événement Spécial</title>
</head>
<body>
    <h1>{{ special_event.title }}</h1>
    <p><strong>Code de l'événement :</strong> {{ special_event.event_code }}</p>
    
    <h2>Inclus dans l'événement</h2>
    {% if included_items %}
        <ul>
            {% for item in included_items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aucun élément inclus.</p>
    {% endif %}

    <h2>Exclus de l'événement</h2>
    {% if excluded_items %}
        <ul>
            {% for item in excluded_items %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Aucun élément exclu.</p>
    {% endif %}

    <!-- Programme quotidien (TourDay) -->
    <h2>Programme</h2>
    {% if special_event.tour_days.count > 0 %}
        <ul>
            {% for day in special_event.tour_days.all %}
                <li>
                    <h3>Jour {{ day.day_number }}</h3>
                    <p><strong>Activité du matin :</strong> {{ day.morning_activity }}</p>
                    <p><strong>Activité de l'après-midi :</strong> {{ day.afternoon_activity }}</p>
                    <p><strong>Activité du soir :</strong> {{ day.evening_activity }}</p>
                </li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Pas de programme pour cet événement.</p>
    {% endif %}

    <!-- Section VIP Pack, Hotel Pack, Tent Pack comme précédemment -->
</body>
</html>





{% endblock content %}


<div class="header-menu">
                            <nav class="main-menu" id="mobile-menu">
                                <ul>
                                    <li class="has-mega-menu">
                                        <a href="index.html">Home</a>
                                        <ul class="mega-menu home-menu-grid">
                                            <li>
                                                <div class="home-menu-item">
                                                    <div class="home-menu-thumb">
                                                        <img src="{% static 'site/images/menu/menu-home-1.jpg' %}"
                                                            alt="thumb not found">
                                                        <div class="home-menu-buttons">
                                                            <a href="home.html" class="bd-primary-btn btn-style">
                                                                <span class="bd-primary-btn-text">Home One</span>
                                                                <span class="bd-primary-btn-circle"></span>
                                                            </a>

                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="home-menu-item">
                                                    <div class="home-menu-thumb">
                                                        <img src="{% static 'site/images/menu/menu-home-2.jpg' %}"
                                                            alt="thumb not found">
                                                        <div class="home-menu-buttons">
                                                            <a href="home-two.html" class="bd-primary-btn btn-style">
                                                                <span class="bd-primary-btn-text">Home Two</span>
                                                                <span class="bd-primary-btn-circle"></span>
                                                            </a>

                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="home-menu-item">
                                                    <div class="home-menu-thumb">
                                                        <img src="{% static 'site/images/menu/menu-home-3.jpg' %}"
                                                            alt="thumb not found">
                                                        <div class="home-menu-buttons">
                                                            <a href="home-three.html" class="bd-primary-btn btn-style">
                                                                <span class="bd-primary-btn-text">Home Three</span>
                                                                <span class="bd-primary-btn-circle"></span>
                                                            </a>

                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="home-menu-item">
                                                    <div class="home-menu-thumb">
                                                        <img src="{% static 'site/images/menu/menu-home-4.jpg' %}"
                                                            alt="thumb not found">
                                                        <div class="home-menu-buttons">
                                                            <a href="home-four.html" class="bd-primary-btn btn-style">
                                                                <span class="bd-primary-btn-text">Home Four</span>
                                                                <span class="bd-primary-btn-circle"></span>
                                                            </a>

                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                            <li>
                                                <div class="home-menu-item">
                                                    <div class="home-menu-thumb">
                                                        <img src="{% static 'site/images/menu/menu-home-5.jpg' %}"
                                                            alt="thumb not found">
                                                        <div class="home-menu-buttons">
                                                            <a href="home-five.html" class="bd-primary-btn btn-style">
                                                                <span class="bd-primary-btn-text">Home Five</span>
                                                                <span class="bd-primary-btn-circle"></span>
                                                            </a>

                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="menu-item-has-children">
                                        <a href="javascript:void(0)">Tour</a>
                                        <ul class="submenu">
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Tour Listing</a>
                                                <ul class="submenu">
                                                    <li><a href="tour-listing.html">Tour Listing Search</a></li>
                                                    <li><a href="tour-listing-two.html">Tour Listing Search 2</a>
                                                    </li>
                                                    <li><a href="tour-listing-three.html">Tour Listing Sidebar</a>
                                                    </li>
                                                    <li><a href="tour-listing-four.html">Tour Listing Full width</a>
                                                    </li>
                                                    <li><a href="tour-listing-five.html">Tour Listing Video</a></li>
                                                    <li><a href="tour-listing-six.html">Tour Listing Banner</a></li>
                                                </ul>
                                            </li>
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Tour Grid</a>
                                                <ul class="submenu">
                                                    <li><a href="tour-grid.html">No Sidebar</a></li>
                                                    <li><a href="tour-grid-right.html">Right Sidebar</a></li>
                                                    <li><a href="tour-grid-left.html">Left Sidebar</a></li>
                                                </ul>
                                            </li>
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Tour Details</a>
                                                <ul class="submenu">
                                                    <li><a href="tour-details.html">No Sidebar</a></li>
                                                    <li><a href="tour-details-right.html">Right Sidebar</a></li>
                                                    <li><a href="tour-details-left.html">Left Sidebar</a></li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="menu-item-has-children">
                                        <a href="javascript:void(0)">Destination</a>
                                        <ul class="submenu">
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Destination Grid</a>
                                                <ul class="submenu">
                                                    <li><a href="destinations-grid.html">No Sidebar</a></li>
                                                    <li><a href="destinations-grid-right.html">Right Sidebar</a>
                                                    </li>
                                                    <li><a href="destinations-grid-left.html">Left Sidebar</a></li>
                                                </ul>
                                            </li>
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Destination Details</a>
                                                <ul class="submenu">
                                                    <li><a href="destinations-details.html">No Sidebar</a></li>
                                                    <li><a href="destinations-details-right.html">Right Sidebar</a>
                                                    </li>
                                                    <li><a href="destinations-details-left.html">Left Sidebar</a>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <!-- page menu -->
                                    <li class="has-mega-menu">
                                        <a href="javascript:void(0)">Pages</a>
                                        <ul class="mega-menu mega-grid-4">
                                            <li>
                                                <a href="javasript:void(0);" class="title">Page Layout 1</a>
                                                <ul>
                                                    <li><a href="about.html">About Us</a></li>
                                                    <li><a href="booking.html">Booking Form</a></li>
                                                    <li><a href="booking-confirm.html">Booking Confirm</a></li>
                                                    <li><a href="pricing.html">Pricing</a></li>
                                                    <li><a href="faq.html">Faq</a></li>
                                                    <li><a href="contact.html">Contact</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">Page Layout 2</a>
                                                <ul>
                                                    <li><a href="team.html">Team</a></li>
                                                    <li><a href="team-details.html">Team Details</a></li>
                                                    <li><a href="error-page.html">Error Page</a></li>
                                                    <li><a href="privacy-policy.html">Privacy & Policy</a></li>
                                                    <li><a href="terms-conditions.html">Terms and Conditions</a>
                                                    </li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">Page Layout 3</a>
                                                <ul>
                                                    <li><a href="dashboard.html">Dashboard</a></li>
                                                    <li><a href="tour-listing-edit.html">Tour Listing Edit</a></li>
                                                    <li><a href="sign-in.html">Login</a></li>
                                                    <li><a href="sign-up.html">Register</a></li>
                                                    <li><a href="forgot.html">Forgot Password</a></li>
                                                    <li><a href="otp.html">OTP</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">Page Layout 4</a>
                                                <ul>
                                                    <li><a href="shop.html">Shop</a></li>
                                                    <li><a href="shop-v2.html">Shop V2</a></li>
                                                    <li><a href="shop-details.html">Shop Details</a></li>
                                                    <li><a href="checkout.html">Checkout</a></li>
                                                    <li><a href="cart.html">Cart</a></li>
                                                    <li><a href="wishlist.html">Wishlist</a></li>
                                                    <li><a href="order.html">Order Confirm</a></li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <!-- elements menu -->
                                    <li class="has-mega-menu">
                                        <a href="javascript:void(0)">Elements</a>
                                        <ul class="mega-menu mega-grid-4">
                                            <li>
                                                <a href="javasript:void(0);" class="title">elements Layout 1</a>
                                                <ul>
                                                    <li><a href="style-guide.html">Style Guide</a></li>
                                                    <li><a href="elements-accordion.html">Accordion</a></li>
                                                    <li><a href="elements-about.html">About Us</a></li>
                                                    <li><a href="elements-advancetab.html">Advance Tab</a></li>
                                                    <li><a href="elements-blog.html">Blog</a></li>
                                                    <li><a href="elements-brand.html">Brand</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">elements Layout 2</a>
                                                <ul>
                                                    <li><a href="elements-breadcrumb.html">Breadcrumb</a></li>
                                                    <li><a href="elements-button.html">Button</a></li>
                                                    <li><a href="elements-cta.html">Call To Action</a></li>
                                                    <li><a href="elements-counter.html">Counter</a></li>
                                                    <li><a href="elements-destinations.html">Destinations</a></li>
                                                    <li><a href="elements-form.html">Form</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">elements Layout 3</a>
                                                <ul>
                                                    <li><a href="elements-footer.html">Footer Style</a></li>
                                                    <li><a href="elements-card.html">Image Card</a></li>
                                                    <li><a href="elements-icomoon.html">Icomoon Fonts Icon</a></li>
                                                    <li><a href="elements-our-offers.html">Offers</a></li>
                                                    <li><a href="elements-pricing.html">Pricing</a></li>
                                                    <li><a href="elements-social.html">Social Share</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="javasript:void(0);" class="title">elements Layout 4</a>
                                                <ul>
                                                    <li><a href="elements-team.html">Team</a></li>
                                                    <li><a href="elements-testimonial.html">Testimonial</a></li>
                                                    <li><a href="elements-tour.html">Tour</a></li>
                                                    <li><a href="elements-why-chose.html">Why Chose Us</a></li>
                                                    <li><a href="#">More Coming</a></li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="menu-item-has-children">
                                        <a href="javascript:void(0)">Blog</a>
                                        <ul class="submenu last-children">
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Blog List</a>
                                                <ul class="submenu">
                                                    <li><a href="blog-list.html">No Sidebar</a></li>
                                                    <li><a href="blog-list-right.html">Right Sidebar</a></li>
                                                    <li><a href="blog-list-left.html">Left Sidebar</a></li>
                                                </ul>
                                            </li>
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Blog Grid</a>
                                                <ul class="submenu">
                                                    <li><a href="blog-grid.html">Blog Grid</a></li>
                                                    <li><a href="blog-grid-right.html">Blog Grid Right</a></li>
                                                    <li><a href="blog-grid-left.html">Blog Grid Left</a></li>
                                                </ul>
                                            </li>
                                            <li class="menu-item-has-children has-arrow">
                                                <a href="javascript:void(0)">Blog Details</a>
                                                <ul class="submenu">
                                                    <li><a href="blog-details.html">No Sidebar</a></li>
                                                    <li><a href="blog-details-right.html">Right sidebar</a></li>
                                                    <li><a href="blog-details-left.html">Left sidebar</a></li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <li><a href="contact.html">Contact</a></li>
                                </ul>
                            </nav>
                        </div>





                         <div class="header-right">
                        <div class="header-action d-flex align-items-center">
                            <div class="header-btn-wrap d-flex align-items-center h-gap-55">
                                <div class="d-none d-sm-inline-flex h-gap-55">
                                    <div class="header-currency-item header-currency">
                                        <span class="header-currency-toggle" id="header-currency-toggle">USD</span>
                                        <ul>
                                            <li>
                                                <a href="#">KWD</a>
                                            </li>
                                            <li>
                                                <a href="#">GBP</a>
                                            </li>
                                            <li>
                                                <a href="#">EUR</a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="d-flex h-gap-55">
                                    <div class="d-xxs-none">
                                        <a class="bd-btn btn-style text-btn color-white" href="contact.html">Help</a>
                                        <a class="bd-btn btn-style text-btn color-white" href="sign-up.html">Sign
                                            up</a>
                                        <a class="bd-btn btn-style text-btn color-white" href="sign-in.html">Sign
                                            in</a>
                                    </div>
                                </div>
                            </div>
                            <div class="header-hamburger ml-20 d-xl-none">
                                <div class="sidebar-toggle">
                                    <a class="bar-icon" href="javascript:void(0)">
                                        <span></span>
                                        <span></span>
                                        <span></span>
                                    </a>
                                </div>
                            </div>
                            <!-- for wp -->
                            <div class="header-hamburger ml-20 d-none">
                                <button type="button" class="hamburger-btn offcanvas-open-btn">
                                    <span>01</span>
                                    <span>01</span>
                                    <span>01</span>
                                </button>
                            </div>
                        </div>
                    </div>
