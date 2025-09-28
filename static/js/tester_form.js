document.addEventListener('DOMContentLoaded', function() {
    const weightInputs = document.querySelectorAll('.weight-input');
    const form = document.getElementById('portfolio_form');
    const errorDiv = document.getElementById('weight-error');

    function validateWeights() {
        let totalWeight = 0;
        weightInputs.forEach(input => {
            const value = parseFloat(input.value) || 0;
            totalWeight += value;
        });

        const roundedTotal = parseFloat(totalWeight.toFixed(2));
        
        if (roundedTotal !== 1) {
            errorDiv.textContent = `The weights must sum to 1. Current sum is ${roundedTotal}.`;
            return false;
        } else {
            errorDiv.textContent = ''; 
            return true;
        }
    }

    weightInputs.forEach(input => {
        input.addEventListener('input', validateWeights);
    });

    form.addEventListener('submit', function(e) {
        if (!validateWeights()) {
            e.preventDefault(); 
        }
    });

    validateWeights();
});


    document.addEventListener('DOMContentLoaded', (event) => {
    const startDateInput = document.getElementById('id_start_date');
    const endDateInput = document.getElementById('id_end_date');
    const startDateErrorSpan = document.getElementById('start-date-error');
    const endDateErrorSpan = document.getElementById('end-date-error');
    const form = document.getElementById('portfolio-form');

    function validateDates() {
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        const minDate = new Date('2015-01-01');
        const maxDate = new Date('2025-09-01');

        let isValid = true;

        startDateErrorSpan.textContent = '';
        endDateErrorSpan.textContent = '';

        if (startDateInput.value && endDateInput.value && startDate > endDate) {
            startDateErrorSpan.textContent = "Start date cannot be after end date.";
            isValid = false;
        }

        if (startDateInput.value && (startDate < minDate || startDate > maxDate)) {
            startDateErrorSpan.textContent = "Date must be between 2015-01-01 and 2025-09-01.";
            isValid = false;
        }
        if (endDateInput.value && (endDate < minDate || endDate > maxDate)) {
            endDateErrorSpan.textContent = "Date must be between 2015-01-01 and 2025-09-01.";
            isValid = false;
        }

        return isValid;
    }

    startDateInput.addEventListener('change', validateDates);
    endDateInput.addEventListener('change', validateDates);

    form.addEventListener('submit', function(e) {
        if (!validateDates()) {
            e.preventDefault();
        }
    });
});