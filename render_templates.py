from django.shortcuts import render
from coachme import models
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse


def renderTemplate(request):
    if 'usercode' in request.session:
        global user_details
        user_code = request.session['usercode']

        user_details = list(models.User.objects.values('name', 'email', 'username', 'user_code', 'about', 'address',
                                                       'profile_pic', 'city', 'country', 'pincode',
                                                       'contact', 'role_id__role_code',
                                                       'role_id__role_name').filter(user_code=user_code))
    try:
        if request.path == '/super_admin_dashboard/':
            return render(request, 'backoffice/superadmin_dashboard.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/user/':
            return render(request, 'backoffice/superadmin_user.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/location/':
            return render(request, 'backoffice/superadmin_location.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/court/':
            return render(request, 'backoffice/superadmin_court.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/report/':
            return render(request, 'backoffice/superadmin_reports.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/sports/':
            return render(request, 'backoffice/superadmin_sports.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/coach/':
            return render(request, 'backoffice/superadmin_coach.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/coachee/':
            return render(request, 'backoffice/superadmin_coachee.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/class/':
            return render(request, 'backoffice/superadmin_class.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/administrator/':
            return render(request, 'backoffice/superadmin_administrator.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/locationManager/':
            return render(request, 'backoffice/superadmin_location_manager.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/class_reviews/':
            return render(request, 'backoffice/superadmin_class_reviews.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/coach_manual_payment/':
            return render(request, 'backoffice/coach_manaulpayment_entry.html', {'userdetails': list(user_details)})

        elif request.path == '/super_admin_dashboard/ledger/':
            return render(request, 'backoffice/superadmin_ledger_report.html', {'userdetails': list(user_details)})

        elif request.path == '/location_manager_dashboard/':
            return render(request, 'backoffice/locationManager_dashboard.html', {'userdetails': list(user_details)})

        elif request.path == '/location_manager_dashboard/user/':
            return render(request, 'backoffice/locationManager_user.html', {'userdetails': list(user_details)})

        elif request.path == '/location_manager_dashboard/classes/':
            return render(request, 'backoffice/locationManager_classes.html', {'userdetails': list(user_details)})

        elif request.path == '/location_manager_dashboard/coaches/':
            return render(request, 'backoffice/locationManager_coach.html', {'userdetails': list(user_details)})

        elif request.path == '/location_manager_dashboard/report/':
            return render(request, 'backoffice/locationManager_report.html', {'userdetails': list(user_details)})

        else:
            # request.session.flush()
            return HttpResponseRedirect('/500-error/')
    except Exception as e:
        print('Exception in method  render_templates.py ---> ', e)
        # request.session.flush()
        return HttpResponseRedirect('/500-error/')
