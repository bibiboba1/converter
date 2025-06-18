document.addEventListener("DOMContentLoaded", function () {
    const rubInput = document.getElementById("inputRUB");
    const czkOutput = document.getElementById("outputCZK");

    rubInput.addEventListener("input", function () {
        const rubValue = parseFloat(rubInput.value);
        const czkValue = rubValue ? (rubValue / 3.75).toFixed(2) : "";
        czkOutput.value = czkValue;
    });
});
