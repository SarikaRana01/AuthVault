
from django.shortcuts import render, redirect
from .forms import *
from .models import Vault
from django.shortcuts import render, redirect, get_object_or_404
from Accounts.models import SignUpModel
from .forms import VaultForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Accounts.utils import encrypt_password,decrypt_password
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse


def show_dashboard(request):
    user = SignUpModel.objects.get(user=request.user)
    entries = Vault.objects.filter(user=user)
    lastEntry=Vault.objects.all().order_by('-created_at').first()
    totalEntries = entries.count()
    uniqueEntries = entries.values('platform').distinct().count()

    show_passwords = {}

    if request.method == "POST":
        entry_id = request.POST.get("entry_id")
        pin_entered = request.POST.get("pin_entered")

        if entry_id and pin_entered:
            account = SignUpModel.objects.get(user=request.user)
            if pin_entered == account.pin:
                entry = Vault.objects.get(id=entry_id)
                decrypted = decrypt_password(entry.encrypted_password)
                show_passwords[int(entry_id)]=decrypted
            else:
                messages.warning(request,"Wrong Pin")
    context = {
       "user":user, "entries": entries, "show_passwords": show_passwords,"totalEntries":totalEntries,"uniqueEntries":uniqueEntries,"lastEntry": lastEntry.created_at if lastEntry else None
    }
    return render(request, "Dashboard/dashboardPage.html", context)

# def show_dashboard(request):
#     user=SignUpModel.objects.filter(user=request.user)
#     entries = Vault.objects.all().order_by('-created_at')
#     lastEntry=Vault.objects.all().order_by('-created_at').first()
#     totalEntries = entries.count()
#     uniqueEntries = entries.values('platform').distinct().count() 
#     context={'user':user,'entries': entries,"totalEntries":totalEntries,"uniqueEntries":uniqueEntries,"lastEntry": lastEntry.created_at if lastEntry else None}
#     return render(request,"Dashboard/dashBoardPage.html",context)





def add_credential(request):
    if request.method == 'POST':
        form = VaultForm(request.POST)

        if form.is_valid():
            vault = form.save(commit=False)
            vault.user = SignUpModel.objects.get(user=request.user)

            raw_password = form.cleaned_data['encrypted_password']
            vault.encrypted_password = encrypt_password(raw_password)

            vault.save()
            messages.success(request, "Credentials Added Successfully")
            return redirect("show")

    else:
        form = VaultForm()
        platform_list = [
            "Facebook", "Instagram", "Twitter (X)", "LinkedIn", "Snapchat",
            "Pinterest", "Reddit", "Quora", "YouTube", "Telegram", "WhatsApp",
            "Discord", "GitHub", "GitLab", "Bitbucket", "Gmail", "Yahoo Mail",
            "Outlook", "ProtonMail", "Zoho Mail", "Amazon", "Flipkart", "Myntra",
            "Snapdeal", "Netflix", "Hotstar (Disney+)", "Spotify", "Zoom",
            "Slack", "Medium"
        ]
        return render(request, 'Dashboard/addPage.html', {
            'form': form,
            'platform_list': platform_list
        })

    # In case of invalid POST, re-render with form errors
    return render(request, 'Dashboard/addPage.html', {'form': form})





def update_credential(request, pk):
    credential = get_object_or_404(Vault, pk=pk)
    if request.method == 'POST':
        form = VaultForm(request.POST, instance=credential)
        if form.is_valid():
            form.save()
            messages.success(request, "Credentials Updated.")
            return redirect('show')  
    else:
        form = VaultForm(instance=credential)

    platform_list = ["Facebook", "Instagram", "Twitter", "LinkedIn", "Email", "Others"]
    return render(request, 'Dashboard/updatePage.html', { 'form': form, 'platform_list': platform_list })



def delete_credential(request, pk):
    credential = get_object_or_404(Vault, pk=pk)
    form = VaultForm(request.POST, instance=credential)
    if request.method == 'POST':
        credential.delete()
        messages.warning(request, "Credentials Deleted!")
        return redirect('show')
    return render(request, 'Dashboard/deletePage.html', {'object': credential,"form":form})





