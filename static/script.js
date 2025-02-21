document.addEventListener("DOMContentLoaded", () => {
    // Category filter functionality
    const filterButtons = document.querySelectorAll(".category-filters .btn")
    const categoryItems = document.querySelectorAll(".category-item")
  
    filterButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const filter = button.getAttribute("data-filter")
  
        filterButtons.forEach((btn) => btn.classList.remove("active"))
        button.classList.add("active")
  
        categoryItems.forEach((item) => {
          if (filter === "all" || item.getAttribute("data-category") === filter) {
            item.style.display = "block"
          } else {
            item.style.display = "none"
          }
        })
      })
    })
  
    // Store rating functionality
    const storeCards = document.querySelectorAll(".store-card")
    storeCards.forEach((card) => {
      const rating = Number.parseFloat(card.querySelector(".store-rating").getAttribute("data-rating"))
      const starsElement = card.querySelector(".stars")
  
      let starsHTML = ""
      for (let i = 1; i <= 5; i++) {
        if (i <= rating) {
          starsHTML += '<i class="bi bi-star-fill"></i>'
        } else if (i - 0.5 <= rating) {
          starsHTML += '<i class="bi bi-star-half"></i>'
        } else {
          starsHTML += '<i class="bi bi-star"></i>'
        }
      }
      starsElement.innerHTML = starsHTML
    })
  
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault()
        const target = document.querySelector(this.getAttribute("href"))
        if (target) {
          target.scrollIntoView({
            behavior: "smooth",
          })
        }
      })
    })
  
    // Add to cart functionality (placeholder)
    const addToCartButtons = document.querySelectorAll(".btn-add-to-cart")
    let cartCount = 0
  
    addToCartButtons.forEach((button) => {
      button.addEventListener("click", () => {
        cartCount++
        updateCartBadge()
      })
    })
  
    function updateCartBadge() {
      const badge = document.querySelector(".badge")
      if (badge) {
        badge.textContent = cartCount
        badge.classList.add("bounce")
        setTimeout(() => badge.classList.remove("bounce"), 300)
      }
    }
  })
  
  