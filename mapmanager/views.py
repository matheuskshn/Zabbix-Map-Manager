from django.shortcuts import render, redirect
from .forms import CreateMapForm
from .zabbix_api import createMap

def create_map_view(request):
    if request.method == 'POST':
        form = CreateMapForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = createMap.main(
                data['map_name'], data['map_groups'], data['map_hosts'], data['map_ips'], 
                data['map_hosts_filter'], data['create_link'], data['add_trigger'], 
                data['unavailable_by_icmp'], data['snmp_not_responding']
            )
            print(request.POST)

            request.session['map_result'] = result

            return redirect('map_result')
    else:
        form = CreateMapForm()

    return render(request, 'map_form.html', {'form': form})

def map_result_view(request):
    result = request.session.get('map_result', {})
    return render(request, 'map_result.html', {'data': result})
