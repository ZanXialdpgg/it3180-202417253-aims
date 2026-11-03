- Vì sao phải đồng bộ master trước khi PR ?
Đồng bộ với phiên bản mới nhất và nhờ đó phát hiện sớm conflict nếu có.

- Khi nào không được rebase ? 
Không rebase branch chính (master) vì đây là branch được dùng chung chứ không phải cá nhân.

- feature/* khác topic/* ra sao ?
feature/* là branch để thêm chức năng trong khi topic/* là branch linh hoạt hơn, chỉ cần là task cùng một chủ đề.