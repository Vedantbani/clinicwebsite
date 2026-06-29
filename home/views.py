from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment

# Shared treatments data across views
TREATMENTS_DATA = {
    'diabetes-management': {
        "title": "Diabetes Management", "icon": "🌿", 
        "symptoms": "Increased thirst, frequent urination, fatigue, blurred vision.",
        "causes": "Insulin resistance, poor dietary habits, lack of physical activity, chronic stress.",
        "natural_treatment": "Dietary regulation (low-GI foods), herbal juices, hydrotherapy, and specific yoga asanas like Mandukasana."
    },
    'thyroid-care': {
        "title": "Thyroid Care", "icon": "🦋", 
        "symptoms": "Weight gain/loss, fatigue, mood swings, hair thinning, temperature sensitivity.",
        "causes": "Hormonal imbalances, high stress levels, nutritional deficiencies, toxic accumulation.",
        "natural_treatment": "Mud therapy to the neck region, pristine diet alterations, and thyroid-stimulating pranayamas (Ujjayi)."
    },
    'pcod-pcos-therapy': {
        "title": "PCOD / PCOS Therapy", "icon": "🌸", 
        "symptoms": "Irregular periods, acne, weight gain, facial hair growth.",
        "causes": "Hormonal imbalance, insulin resistance, sedentary lifestyle, poor sleep cycles.",
        "natural_treatment": "Detoxification programs, therapeutic fasting, specific stress management, and hip baths."
    },
    'weight-management': {
        "title": "Weight Management", "icon": "🏃‍♂️", 
        "symptoms": "Excess body fat, breathlessness, low energy levels, joint strains.",
        "causes": "Caloric imbalance, metabolic slowdown, hormonal issues, emotional eating.",
        "natural_treatment": "Full body mud packs, steam baths, scientific diet planning (juice fasting/raw diet), and vigorous yoga flows."
    },
    'arthritis-joint-care': {
        "title": "Arthritis & Joint Care", "icon": "🦴", 
        "symptoms": "Joint pain, swelling, stiffness, restricted movement.",
        "causes": "Accumulation of uric acid, wear and tear of cartilage, systemic inflammation.",
        "natural_treatment": "Warm hydrotherapy, local mud applications, castor oil massages, and gentle joint-mobility yoga stretches."
    },
    'stress-anxiety-relief': {
        "title": "Stress & Anxiety Relief", "icon": "🧘", 
        "symptoms": "Restlessness, insomnia, racing thoughts, chronic fatigue.",
        "causes": "Overactive nervous system, work pressure, mental exhaustion, lack of mindfulness.",
        "natural_treatment": "Sirodhara therapy, deep relaxation techniques (Yoga Nidra), meditation pathways, and soothing cold compresses."
    }
}

def home(request):
    # Convert dictionary to list for the homepage grid display
    treatments = [{"slug": slug, **details} for slug, details in TREATMENTS_DATA.items()]
    
    packages = [
        {"name": "Detox & Rejuvenation", "duration": "7 Days", "focus": "Body Purification"},
        {"name": "Diabetes Management Plan", "duration": "15 Days", "focus": "Blood Sugar Control"},
        {"name": "Weight Loss Program", "duration": "30 Days", "focus": "Metabolic Reset"},
        {"name": "Arthritis & Pain Relief", "duration": "21 Days", "focus": "Joint Mobility"}
    ]

    if request.method == "POST":
        user_name = request.POST.get('name')
        user_phone = request.POST.get('phone')
        user_date = request.POST.get('preferred_date')
        user_choice = request.POST.get('therapy_or_package')
        user_notes = request.POST.get('health_notes')

        appointment = Appointment(
            name=user_name, phone=user_phone, preferred_date=user_date,
            therapy_or_package=user_choice, health_notes=user_notes
        )
        appointment.save()
        messages.success(request, f"Thank you {user_name}! Your appointment request has been submitted.")
        return redirect('home')

    context = {
        'treatments': treatments,
        'packages': packages
    }
    return render(request, "home/index.html", context)

# New dynamic detail view
def treatment_detail(request, slug):
    # Fetch data based on the unique URL slug
    treatment = TREATMENTS_DATA.get(slug)
    if not treatment:
        return redirect('home') # Fallback if treatment slug doesn't exist
        
    return render(request, "home/treatment_detail.html", {'treatment': treatment})