$(".add-to-cart-btn").on("click", function(){
    let productContainer = $(this).closest('.item');
    let quantity = productContainer.find(".product-quantity").val();
    let product_title_al = productContainer.find(".product-title-al").val();
    let product_title_en = productContainer.find(".product-title-en").val();
    let product_id = productContainer.find(".product-id").val();
    let product_price = productContainer.find(".product-price").text();
    let this_btn = $(this);



    console.log("Quantity:", quantity);
    console.log("Title (AL):", product_title_al);
    console.log("Title (EN):", product_title_en);
    console.log("ID:", product_id);
    console.log("Price:", product_price);
    console.log("Current Element:", this_btn);

    $.ajax({
        url: '/add-to-cart/',
        data: {
            'id': product_id,
            'qty': quantity,
            'title_al': product_title_al,
            'title_en': product_title_en,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding product to cart...");
        },
        success: function(response){
            this_btn.html("<i class=\"fa-solid fa-check\"></i>").css("font-size", "20px");
            console.log("Product added");
            $('.cart-items-count').text(response.totalcartitems);
        }
    });
});



$(".delete-product").on('click', function (){
    let product_id = $(this).attr("data-product");
    let this_val = $(this);

    console.log("Product ID:", product_id, "Deleted");

    $.ajax({
        url: "/delete-item-from-cart/",
        data: {
            "id": product_id
        },
        dataType: "json",
        beforeSend: function (){
            this_val.hide();
        },
        success: function (response){
            this_val.show();
            $('.cart-items-count').text(response.totalcartitems);
            $('#cart-list').html(response.data);
            location.reload(true);
        }
    });
});


$(".update-product").on('click', function (){
    let product_id = $(this).attr("data-product");
    let this_val = $(this);
    let product_qty = $('.product-qty-' + product_id).val();

    console.log("Product ID:", product_id, "Deleted");
    console.log("Product QTY:", product_qty);

    $.ajax({
        url: "/update-cart/",
        data: {
            "id": product_id,
            "qty": product_qty
        },
        dataType: "json",
        beforeSend: function (){
            this_val.hide();
        },
        success: function (response){
            this_val.show();
            $('.cart-items-count').text(response.totalcartitems);
            $('#cart-list').html(response.data);
            location.reload(true);
        }
    });
});