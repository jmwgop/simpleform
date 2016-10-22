var conditional_fields = $("div.royalty");
conditional_fields.hide();

}$(".ogml").change(function() {
    if ($(this).prop('checked') === 'checked') {
        conditional_fields.show();
    } else {
        conditional_fields.hide();
    }
});
