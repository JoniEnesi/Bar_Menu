setTimeout(function() {
   location.reload();
}, 30000);



document.addEventListener('DOMContentLoaded', function() {
   var tabela = document.getElementById('result_list');
   var rreshtat = tabela.querySelectorAll('tbody tr');

   rreshtat.forEach(function(rreshti) {

       var inputOrderView = rreshti.querySelectorAll('input[id^="id_form-"][id$="-view_order"]');

       inputOrderView.forEach(function(input) {
           input.insertAdjacentHTML('afterend', '<input type="submit" name="_save" class="btn btn-sm btn-success" value="Save">');
       });


       var inputIsPaid = rreshti.querySelectorAll('input[id^="id_form-"][id$="-is_paid"]');

       inputIsPaid.forEach(function(input) {
           input.insertAdjacentHTML('afterend', '<input type="submit" name="_save" class="btn btn-sm btn-success" value="Save">');
       });

   });
});



$(document).ready(function(){
    var aTag = $('.field-get_table a');
    var pTag = $('<p></p>').html(aTag.html());
    aTag.replaceWith(pTag);
});



document.addEventListener('DOMContentLoaded', function() {
    var targetElements = document.getElementsByClassName('field-__str__');
    if (targetElements.length > 0) {
        var targetElement = targetElements[0];

        var link = document.createElement('a');
        link.innerText = 'Print Daily Summary';
        link.href = '/daily-summary/';
        link.style.padding = '10px';
        link.style.backgroundColor = '#007bff';
        link.style.color = '#fff';
        link.style.borderRadius = '5px';
        link.style.textDecoration = 'none';

        targetElement.appendChild(link);
    }
});