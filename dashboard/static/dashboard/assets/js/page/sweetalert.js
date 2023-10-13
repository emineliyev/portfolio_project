"use strict";

$(".swal").click(function (event) {
    event.preventDefault();
    const businessId = $(this).data('business-id');
    const partnerId = $(this).data('partner-id');
    const portfolioId = $(this).data('portfolio-id');
    const categoryId = $(this).data('category-id');
    const sliderId = $(this).data('slider-id');
    const serviceTypeId = $(this).data('services_type-id');
    const teamId = $(this).data('team-id');
    const iconId = $(this).data('icon-id');
    const phoneId = $(this).data('phone-id');
    const emailId = $(this).data('email-id');

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
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/partner_delete/${partnerId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/email_delete/${emailId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/phone_delete/${phoneId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/category_delete/${categoryId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {

                        if (data.error) {
                            swal('Xəta!', data.error, 'error')
                        } else {
                            swal('Melumatlar uğurla silindi', {
                                icon: 'success'
                            })
                            setTimeout(function () {
                                location.reload()
                            }, 2000)
                        }
                    }
                });

                $.ajax({
                    url: `/icon_delete/${iconId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/team_delete/${teamId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/slider_delete/${sliderId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/service_type_delete/${serviceTypeId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
                $.ajax({
                    url: `/portfolio_delete/${portfolioId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}'
                    },
                    success: function (data) {
                        swal('Məlumatlar uğurla silindi', {
                            icon: 'success',
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2000)
                    }
                });
            }
        });

});