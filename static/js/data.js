
// function listing() {
//     $.ajax({
//         type: "GET",
//         url: "/get-posts-meeting",
//         data: {},
//         success: function (response) {
//             let data = response["data"];
//             for (let i = 0; i < data.length; i++) {
//                 let nama = data[i]["Nama"];
//                 let telepon = data[i]["Telepon"];
//                 let komunitas = data[i]["Komunitas"];
//                 let tanggal = data[i]["Tanggal"];
//                 let waktu = data[i]["Jam"];
//                 let durasi = data[i]["Durasi"];
//                 let jumlah = data[i]["jumlah orang"];
//                 let pilih = data[i]["Area"];
//                 let dp = data[i]["dp"];

//                 let temp_html = `
                
               
//                 <tr>
//                     <td>${nama}</td>
//                     <td>${telepon}</td>
//                     <td>${komunitas}</td>
//                     <td>${tanggal}</td>
//                     <td>${waktu}</td>
//                     <td>${durasi}</td>
//                     <td>${jumlah}</td>
//                     <td>${pilih}</td>
//                     <td>${dp}</td>
//                 </tr>        `;
//                 $("#meeting-box").append(temp_html);
//             }
//         },
//     });

// }

