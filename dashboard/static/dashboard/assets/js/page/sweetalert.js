"use strict";

$(".swal").click(function (event) {
    event.preventDefault();
    const businessId = $(this).data('business-id');
    const partnerId = $(this).data('partner-id');

    swal({
        title: 'Siz əminsiniz?',
        text: 'Sildikdən sonra bərpa edə bilməyəcəksiniz!',
        icon: 'warning',
        buttons: true,
        dangerMode: true,
    })
        .then((willDelete) => {
            if (willDelete) {
                $.ajax({
                    url: `/business_plan_delete/${businessId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    },
                    error: function (error) {
                        swal('Məlumatlar silinmədi!');
                    }
                });
                $.ajax({
                    url: `/partner_delete/${partnerId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    },
                    error: function (error) {
                        swal('Məlumatlar silinmədi!');
                    }
                });
            }
        });

});