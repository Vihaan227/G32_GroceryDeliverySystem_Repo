// Enhanced store data with more stores
const stores = [
  {
    name: "FoodsCo",
    logo: "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Screenshot%202025-02-20%20at%201.33.54%E2%80%AFAM-Nd6pc5ivEVBMSRQaFsxLrX6mI1AZ2u.png",
    deliveryTime: "12:30pm",
    distance: "2.0 mi",
    priceRange: "$",
    categories: ["Pantry", "Dairy", "Frozen Food"],
    promotions: ["$5 off"],
    features: ["EBT", "Low prices", "Loyalty savings"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 35,
    rating: 4.7,
    tags: ["eco-friendly"]
  },
  {
    name: "Costco",
    logo: "https://upload.wikimedia.org/wikipedia/commons/5/59/Costco_logo.svg",
    deliveryTime: "2:00pm",
    distance: "1.6 mi",
    priceRange: "$",
    categories: ["Groceries", "Wholesale"],
    promotions: [],
    features: ["EBT", "Loyalty savings", "Bulk pricing"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 60,
    rating: 4.9,
    tags: ["wholesale"]
  },
  {
    name: "Safeway",
    logo: "https://upload.wikimedia.org/wikipedia/commons/c/ce/Safeway_Logo.svg",
    deliveryTime: "12:25pm",
    distance: "0.5 mi",
    priceRange: "$$",
    categories: ["Groceries", "Bakery", "Deli"],
    promotions: [],
    features: ["EBT", "Lots of deals"],
    hasLightningDelivery: true,
    hasPickup: true,
    estimatedDeliveryMinutes: 30,
    rating: 4.5,
    tags: ["pharmacy"]
  },
  {
    name: "Grocery Outlet",
    logo: "https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/0017/5918/brand.gif",
    deliveryTime: "1:45pm",
    distance: "2.8 mi",
    priceRange: "$",
    categories: ["Groceries", "Organic", "Alcohol"],
    promotions: [],
    features: ["Low prices"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 55,
    rating: 4.2,
    tags: ["bargain"]
  },
  {
    name: "FoodsCo Delivery Now",
    logo: "https://cdn.icon-icons.com/icons2/2785/PNG/512/delivery_icon_177568.png",
    deliveryTime: "12:20pm",
    distance: "2.0 mi",
    priceRange: "$",
    categories: ["Groceries", "Organic"],
    promotions: [],
    features: ["Get a few things fast", "EBT", "Low prices"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 25,
    rating: 4.6,
    tags: ["express"]
  },
  {
    name: "Restaurant Depot",
    logo: "https://www.restaurantdepot.com/media/logo/websites/1/logo.png",
    deliveryTime: "2:00pm",
    distance: "2.9 mi",
    priceRange: "$",
    categories: ["Pantry", "Meat", "Dairy"],
    promotions: [],
    features: ["Bulk pricing"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 65,
    rating: 4.4,
    tags: ["wholesale", "bulk"]
  },
  {
    name: "Walmart",
    logo: "https://cdn.worldvectorlogo.com/logos/walmart.svg",
    deliveryTime: "3:00pm",
    distance: "35.8 mi",
    priceRange: "$",
    categories: ["Groceries", "Home", "Electronics"],
    promotions: [],
    features: ["In-store prices", "Low prices"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 90,
    rating: 4.1,
    tags: ["supercenter"]
  },
  {
    name: "Luke's Local",
    logo: "https://cdn.shopify.com/s/files/1/0336/7167/5948/t/49/assets/image-4-1663166121628.svg",
    deliveryTime: "12:25pm",
    distance: "1.1 mi",
    priceRange: "$$$",
    categories: ["Local Produce", "Artisanal", "Organic"],
    promotions: [],
    features: ["Farm fresh", "Local businesses"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 35,
    rating: 4.8,
    tags: ["local", "sustainable"]
  },
  {
    name: "Target: Fast Delivery",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Target_Corporation_logo_%28vector%29.svg/1200px-Target_Corporation_logo_%28vector%29.svg.png",
    deliveryTime: "12:20pm",
    distance: "0.7 mi",
    priceRange: "$$",
    categories: ["Groceries", "Home Goods", "Essentials"],
    promotions: [],
    features: ["Get a few things fast"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 20,
    rating: 4.6,
    tags: ["express"]
  },
  {
    name: "99 Ranch Market",
    logo: "https://cdn-carrefouruae.sslcs.cdngc.net/images/99-ranch-market-logo.jpg",
    deliveryTime: "2:00pm",
    distance: "8.9 mi",
    priceRange: "$$",
    categories: ["Pantry", "Fresh Produce", "Meat"],
    promotions: ["$6 off"],
    features: ["International foods", "Fresh seafood"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 70,
    rating: 4.7,
    tags: ["asian", "international"]
  },
  {
    name: "Lucky Supermarkets",
    logo: "https://upload.wikimedia.org/wikipedia/commons/0/0f/Lucky_Supermarkets_logo.svg",
    deliveryTime: "12:30pm",
    distance: "3.0 mi",
    priceRange: "$$",
    categories: ["Groceries", "Produce", "Organic"],
    promotions: ["$15 off"],
    features: ["In-store prices", "EBT", "Lots of deals"],
    hasLightningDelivery: true,
    hasPickup: true,
    estimatedDeliveryMinutes: 40,
    rating: 4.3,
    tags: ["deals"]
  },
  {
    name: "Safeway Rapid",
    logo: "https://upload.wikimedia.org/wikipedia/commons/c/ce/Safeway_Logo.svg",
    deliveryTime: "12:20pm",
    distance: "0.5 mi",
    priceRange: "$$",
    categories: ["Essential Groceries", "Ready Meals"],
    promotions: [],
    features: ["Get a few things fast", "Lots of deals"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 15,
    rating: 4.4,
    tags: ["express"]
  },
  // New stores added below
  {
    name: "Trader Joe's",
    logo: "https://www.traderjoes.com/content/dam/trjo/icons/tj-logo.svg",
    deliveryTime: "1:15pm",
    distance: "1.7 mi",
    priceRange: "$$",
    categories: ["Organic", "Specialty Foods", "Prepared Meals"],
    promotions: [],
    features: ["Unique items", "Friendly staff"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 45,
    rating: 4.8,
    tags: ["organic", "specialty"]
  },
  {
    name: "Whole Foods Market",
    logo: "https://upload.wikimedia.org/wikipedia/commons/a/a2/Whole_Foods_Market_201x_logo.svg",
    deliveryTime: "1:00pm",
    distance: "2.2 mi",
    priceRange: "$$$",
    categories: ["Organic", "Natural Foods", "Prepared Foods"],
    promotions: ["Prime discount"],
    features: ["Premium quality", "Sustainable"],
    hasLightningDelivery: true,
    hasPickup: true,
    estimatedDeliveryMinutes: 40,
    rating: 4.7,
    tags: ["organic", "premium"]
  },
  {
    name: "Sprouts Farmers Market",
    logo: "https://upload.wikimedia.org/wikipedia/commons/0/0a/Sprouts_Farmers_Market_logo.svg",
    deliveryTime: "1:30pm",
    distance: "3.4 mi",
    priceRange: "$$",
    categories: ["Fresh Produce", "Organic", "Supplements"],
    promotions: ["20% off produce"],
    features: ["Farmer's market feel", "Bulk bins"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 50,
    rating: 4.5,
    tags: ["health", "organic"]
    
  },
  {
    name: "H Mart",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/H_Mart_logo.svg/512px-H_Mart_logo.svg.png",
    deliveryTime: "2:15pm",
    distance: "5.1 mi",
    priceRange: "$$",
    categories: ["Asian Groceries", "Produce", "Seafood"],
    promotions: [],
    features: ["International specialties", "Fresh seafood"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 65,
    rating: 4.6,
    tags: ["asian", "international"]
  },
  {
    name: "Aldi",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Aldi_logo.svg/640px-Aldi_logo.svg.png",
    deliveryTime: "1:25pm",
    distance: "4.2 mi",
    priceRange: "$",
    categories: ["Groceries", "Household", "Seasonal"],
    promotions: [],
    features: ["Budget friendly", "Weekly specials"],
    hasLightningDelivery: true,
    estimatedDeliveryMinutes: 55,
    rating: 4.3,
    tags: ["budget", "european"]
  },
  {
    name: "Kroger Express",
    logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Kroger_logo.svg/1200px-Kroger_logo.svg.png",
    deliveryTime: "12:40pm",
    distance: "1.3 mi",
    priceRange: "$$",
    categories: ["Groceries", "Pharmacy", "Deli"],
    promotions: ["First order free delivery"],
    features: ["Digital coupons", "Fuel points"],
    hasLightningDelivery: true,
    hasPickup: true,
    estimatedDeliveryMinutes: 30,
    rating: 4.5,
    tags: ["express"]
  }
];

// Interactive features for the enhanced page
document.addEventListener("DOMContentLoaded", function() {
  initializeUI();
  initializeStoreGrid();
  initializeInteractiveFeatures();
});

function initializeUI() {
  // Add interactive heading
  const mainContainer = document.querySelector('.container');
  
  // Create and insert header section before the existing content
  const headerSection = document.createElement('div');
  headerSection.className = 'page-header';
  headerSection.innerHTML = `
    <h1 class="page-title">Fresh Food, Fast Delivery</h1>
    <div class="filter-container">
      <button class="filter-button active" data-filter="all">All Stores</button>
      <button class="filter-button" data-filter="express">Express Delivery</button>
      <button class="filter-button" data-filter="organic">Organic & Natural</button>
      <button class="filter-button" data-filter="ebt">EBT Accepted</button>
      <button class="filter-button" data-filter="pickup">Pickup Available</button>
      <button class="filter-button" data-filter="international">International Foods</button>
    </div>
  `;
  
  // Insert the header before the existing content
  const storeGrid = document.getElementById('store-grid');
  mainContainer.insertBefore(headerSection, storeGrid);
  
  // Add scroll to top button
  const scrollTopButton = document.createElement('div');
  scrollTopButton.className = 'scroll-top';
  scrollTopButton.innerHTML = '<i class="bi bi-arrow-up"></i>';
  document.body.appendChild(scrollTopButton);
}

function createStoreCard(store, index) {
  const template = document.getElementById("store-card-template") || createCardTemplate();
  const card = template.content.cloneNode(true);
  const storeCard = card.querySelector(".store-card");
  
  // Set animation delay based on index
  storeCard.style.animationDelay = `${index * 0.1}s`;
  
  // Add data attributes for filtering
  if (store.tags) {
    storeCard.setAttribute('data-tags', store.tags.join(' '));
  }
  if (store.hasPickup) {
    storeCard.setAttribute('data-pickup', 'true');
  }
  if (store.features && store.features.includes('EBT')) {
    storeCard.setAttribute('data-ebt', 'true');
  }
  
  // Set store logo and name
  card.querySelector(".store-logo").src = store.logo;
  card.querySelector(".store-logo").alt = `${store.name} logo`;
  card.querySelector(".store-name").textContent = store.name;

  // Add rating if available
  if (store.rating) {
    const nameElement = card.querySelector(".store-name");
    const ratingSpan = document.createElement('span');
    ratingSpan.className = 'store-rating';
    ratingSpan.innerHTML = `<i class="bi bi-star-fill text-warning"></i> ${store.rating}`;
    ratingSpan.style.fontSize = '0.875rem';
    ratingSpan.style.marginLeft = '0.5rem';
    ratingSpan.style.fontWeight = 'normal';
    nameElement.appendChild(ratingSpan);
  }

  // Set delivery info
  const deliveryInfo = card.querySelector(".delivery-info");
  let deliveryHtml = '';
  
  if (store.hasLightningDelivery) {
    deliveryHtml += `<i class="bi bi-lightning-fill"></i> Delivery by ${store.deliveryTime}`;
  }
  
  deliveryHtml += ` • ${store.distance} • ${store.priceRange}`;
  deliveryInfo.innerHTML = deliveryHtml;
  
  // Add estimated delivery time
  if (store.estimatedDeliveryMinutes) {
    const timeIndicator = document.createElement('div');
    timeIndicator.className = 'delivery-time-indicator';
    timeIndicator.innerHTML = `<i class="bi bi-clock"></i> ${store.estimatedDeliveryMinutes} min`;
    timeIndicator.style.fontSize = '0.75rem';
    timeIndicator.style.color = '#666';
    timeIndicator.style.marginTop = '0.25rem';
    card.querySelector(".delivery-details").appendChild(timeIndicator);
  }
  
  // Add pickup available if applicable
  if (store.hasPickup) {
    const pickupInfo = document.createElement('p');
    pickupInfo.className = "pickup-info";
    pickupInfo.innerHTML = `<i class="bi bi-building"></i> Pickup available`;
    card.querySelector(".delivery-details").appendChild(pickupInfo);
  }

  // Set categories
  if (store.categories && store.categories.length > 0) {
    card.querySelector(".categories").textContent = store.categories.join(" • ");
  } else {
    card.querySelector(".categories").remove();
  }

  // Add promotions
  const promotionsDiv = card.querySelector(".promotions");
  if (store.promotions && store.promotions.length > 0) {
    store.promotions.forEach((promo) => {
      const tag = document.createElement("span");
      tag.className = "tag promotion-tag";
      tag.textContent = promo;
      promotionsDiv.appendChild(tag);
    });
  } else {
    promotionsDiv.remove();
  }

  // Add features
  const featuresDiv = card.querySelector(".features");
  if (store.features && store.features.length > 0) {
    store.features.forEach((feature) => {
      const tag = document.createElement("span");
      tag.className = "tag feature-tag";
      tag.textContent = feature;
      featuresDiv.appendChild(tag);
    });
  } else {
    featuresDiv.remove();
  }

  return card;
}

function createCardTemplate() {
  // Create template element if it doesn't exist
  const template = document.createElement('template');
  template.id = 'store-card-template';
  template.innerHTML = `
    <div class="store-card">
      <div class="d-flex align-items-center mb-3">
        <div class="store-logo-wrapper me-3">
          <img src="/placeholder.svg" alt="" class="store-logo">
        </div>
        <div>
          <h3 class="store-name mb-0"></h3>
        </div>
      </div>
      <div class="delivery-details mb-2">
        <p class="delivery-info mb-1"></p>
        <!-- Pickup info will be added here if applicable -->
      </div>
      <p class="categories mb-2"></p>
      <div class="tags promotions mb-2"></div>
      <div class="tags features"></div>
    </div>
  `;
  document.body.appendChild(template);
  return template;
}

function initializeStoreGrid() {
  const grid = document.getElementById("store-grid");
  grid.innerHTML = '';  // Clear existing content
  
  stores.forEach((store, index) => {
    setTimeout(() => {
      const card = createStoreCard(store, index);
      grid.appendChild(card);
    }, index * 50); // Faster stagger for smoother experience
  });
}

function initializeInteractiveFeatures() {
  // Filter buttons functionality
  const filterButtons = document.querySelectorAll('.filter-button');
  filterButtons.forEach(button => {
      button.addEventListener('click', function() {
          // Remove active class from all buttons
          filterButtons.forEach(btn => btn.classList.remove('active'));
          
          // Add active class to clicked button
          this.classList.add('active');
          
          // Apply filter
          const filter = this.getAttribute('data-filter');
          filterStoresByCategory(filter);
      });
  });
  
  // Interactive heading
  const pageTitle = document.querySelector('.page-title');
  if (pageTitle) {
      pageTitle.addEventListener('click', function() {
          // Reset all filters
          filterButtons.forEach(btn => btn.classList.remove('active'));
          document.querySelector('[data-filter="all"]').classList.add('active');
          showAllStores();
          
          // Add a small animation
          this.style.transition = "transform 0.3s ease-in-out";
          this.style.transform = "scale(1.1)";
          
          setTimeout(() => {
              this.style.transform = "scale(1)";
          }, 300);
      });
  }
}

function filterStoresByCategory(category) {
  const storeCards = document.querySelectorAll('.store-card');
  
  storeCards.forEach(card => {
      if (category === 'all') {
          card.style.display = 'block';
          return;
      }
      
      // Handle special filters
      switch(category) {
          case 'express':
              if (card.querySelector('.delivery-time-indicator') && 
                  parseInt(card.querySelector('.delivery-time-indicator').textContent) <= 30) {
                  card.style.display = 'block';
              } else {
                  card.style.display = 'none';
              }
              break;
          case 'ebt':
              if (card.hasAttribute('data-ebt')) {
                  card.style.display = 'block';
              } else {
                  card.style.display = 'none';
              }
              break;
          case 'pickup':
              if (card.hasAttribute('data-pickup')) {
                  card.style.display = 'block';
              } else {
                  card.style.display = 'none';
              }
              break;
          case 'organic':
              if (card.getAttribute('data-tags') && 
                  (card.getAttribute('data-tags').includes('organic') || 
                   card.getAttribute('data-tags').includes('sustainable'))) {
                  card.style.display = 'block';
              } else {
                  card.style.display = 'none';
              }
              break;
          case 'international':
              if (card.getAttribute('data-tags') && 
                  card.getAttribute('data-tags').includes('international')) {
                  card.style.display = 'block';
              } else {
                  card.style.display = 'none';
              }
              break;
          default:
              card.style.display = 'block';
      }
  });
}

function showAllStores() {
  const storeCards = document.querySelectorAll('.store-card');
  storeCards.forEach(card => {
      card.style.display = 'block';
  });
}