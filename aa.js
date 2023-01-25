<script>
var num = document.documentElement.innerText.match(/(品番 : ).*/)[0].substr(5);
var price = document.getElementsByClassName('price')[1].innerText.replace(/[^0-9]/g, '');
var c_id = document.getElementById('other_' + $('input[name=classcategory_id1]').val()).getElementsByTagName('a')[0].getAttribute('href')
var color = c_id.substr(c_id.search('_')+1);
var prod_id = num + '-' + color;

var google_tag_params = {
    ecomm_prodid: 'prod_id';
    ecomm_pagetype: 'product';
    ecomm_totalvalue: 'price';
}
</script>