    
    // $('#pdf-button').on('click', function(){
    //     console.log('test')
    // });

    function genPDF() {
        var doc = new jsPDF('p', 'mm', 'a4');      
        




        // doc.setFont('PTSans'); // set custom font
        // doc.setFontSize(18); // you can change size
        // doc.text("A", 15, 15);
        doc.addPage();     





        
        const pageCount = doc.internal.getNumberOfPages();
        for(var i = 1; i <= pageCount; i++){
            doc.setPage(i);

            /* HEADER */
            doc.setFont('Arial');
            doc.setFontSize(12);
            doc.text('Outreach Productions', 10, 25);            
            doc.line(203, 28, 8, 28); // width, right, ,left

            /* HEADER IMAGE */
            var img = new Image()
            img.src = 'static/images/OPLogo.png'
            doc.addImage(img, 'png', 135, 10, 60, 15)            



            /* FOOTER */
            doc.line(203, 280, 8, 280);

            /* FOOTER LEFT */
            doc.setFont('Arial');
            doc.setFontSize(12);
            doc.text('Rommel Martinez', 10, 285);

            /* FOOTER RIGHT */
            doc.setFont('Arial');
            doc.setFontSize(12);
            doc.text('Page ' + String(i) + ' of ' + String(pageCount), 180, 285, null, null);
        }





        // doc.fromHTML($('#frm').html(), 15, 15);

        // doc.autoPrint();
        // doc.output("dataurlnewwindow");
        window.open(URL.createObjectURL(doc.output("blob")))
    }


