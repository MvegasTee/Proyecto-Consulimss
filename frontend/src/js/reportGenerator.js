// Importar jsPDF desde el módulo
import { jsPDF } from "jspdf";

document.getElementById("generate-pdf").addEventListener("click", function () {
    // Obtener los datos del formulario
    const templateName = document.getElementById("template-name").value;
    const reportType = document.querySelector('input[name="template"]:checked').nextElementSibling.textContent;
    const customText = document.getElementById("custom-text").value;

    // Validar que todos los campos estén completos
    if (!templateName || !customText) {
        alert("Por favor, completa todos los campos antes de generar el reporte.");
        return;
    }

    // Crear un nuevo documento PDF
    const pdf = new jsPDF();

    // Agregar contenido al PDF
    pdf.setFont("Helvetica", "normal");
    pdf.setFontSize(16);
    pdf.text(templateName, 10, 20);
    pdf.setFontSize(12);
    pdf.text(`Tipo de Reporte: ${reportType}`, 10, 30);
    pdf.text("Descripción:", 10, 40);
    pdf.text(customText, 10, 50, { maxWidth: 190 });

    // Generar URL para vista previa
    const pdfBlob = pdf.output("blob");
    const pdfURL = URL.createObjectURL(pdfBlob);
    document.getElementById("pdf-preview").src = pdfURL;
});
