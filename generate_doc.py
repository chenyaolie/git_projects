from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Cm

def add_heading_style(doc, level, text):
    heading = doc.add_heading(text, level)
    run = heading.runs[0]
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    if level == 1:
        run.font.size = Pt(16)
        run.font.bold = True
    elif level == 2:
        run.font.size = Pt(14)
        run.font.bold = True
    elif level == 3:
        run.font.size = Pt(12)
        run.font.bold = True
    return heading

def add_normal_paragraph(doc, text, indent=False):
    para = doc.add_paragraph(text)
    para.paragraph_format.line_spacing = Pt(18)
    if text.strip():
        run = para.runs[0]
        run.font.name = '宋体'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        run.font.size = Pt(12)
    if indent:
        para.paragraph_format.first_line_indent = Cm(0.74)
    return para

def create_document():
    doc = Document()
    
    style = doc.styles['Normal']
    style.font.name = '宋体'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    style.font.size = Pt(12)
    
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.25)
    
    title = doc.add_heading('餐饮消费管理系统软件开发文档', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title.runs[0]
    title_run.font.name = '黑体'
    title_run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    title_run.font.size = Pt(22)
    
    doc.add_paragraph()
    
    info_table = doc.add_table(rows=6, cols=2)
    info_table.style = 'Table Grid'
    info_table.cell(0, 0).text = '项目名称'
    info_table.cell(0, 1).text = '餐饮消费管理系统'
    info_table.cell(1, 0).text = '项目类型'
    info_table.cell(1, 1).text = '综合性 设计性 应用性'
    info_table.cell(2, 0).text = '课程名称'
    info_table.cell(2, 1).text = 'Java EE框架技术'
    info_table.cell(3, 0).text = '专业班级'
    info_table.cell(3, 1).text = '软工2301班'
    info_table.cell(4, 0).text = '开发日期'
    info_table.cell(4, 1).text = '2026年6月'
    info_table.cell(5, 0).text = '开发团队'
    info_table.cell(5, 1).text = 'HGNU开发组'
    
    for row in info_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    doc.add_page_break()
    
    doc.add_heading('目  录', 1)
    toc_content = [
        ('第1章 绪论', '1'),
        ('1.1 研究背景', '1'),
        ('1.2 发展现状', '3'),
        ('1.3 研究意义', '5'),
        ('1.4 主要工作', '7'),
        ('第2章 需求分析', '9'),
        ('2.1 性能需求', '9'),
        ('2.2 功能模块需求', '11'),
        ('2.3 本章小结', '18'),
        ('第3章 总体设计', '19'),
        ('3.1 功能模块结构设计', '19'),
        ('3.2 技术架构设计', '21'),
        ('3.3 技术架构层次设计', '23'),
        ('3.4 数据库设计', '25'),
        ('3.5 本章小结', '35'),
        ('第4章 详细设计及实现', '36'),
        ('4.1 开发环境的搭建', '36'),
        ('4.2 学生模块的设计与实现', '38'),
        ('4.3 员工模块的设计与实现', '48'),
        ('4.4 管理员模块的设计与实现', '58'),
        ('4.5 本章小结', '70'),
        ('第5章 测试', '71'),
        ('5.1 学生模块功能测试', '71'),
        ('5.2 员工模块功能测试', '75'),
        ('5.3 管理员模块功能测试', '79'),
        ('5.4 本章小结', '85'),
        ('总  结', '86'),
        ('参考文献', '88'),
        ('附  录', '90')
    ]
    
    for item in toc_content:
        toc_line = doc.add_paragraph()
        toc_line.add_run(item[0]).font.name = '宋体'
        toc_line.add_run(' ' * (60 - len(item[0]))).font.name = '宋体'
        toc_line.add_run(item[1]).font.name = '宋体'
        toc_line.runs[0]._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        toc_line.runs[1]._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        toc_line.runs[2]._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '第1章 绪论')
    add_normal_paragraph(doc, '本章从餐饮消费管理系统（Dining Expense Management System，简称DEMS）的研究背景和意义出发，论述了高校餐饮消费管理系统设计与实现的迫切性，总结和概述了现阶段国内外高校餐饮消费管理系统的发展现状，其中重点介绍了餐饮消费管理系统的实现为高校师生和管理人员带来的便利，在此基础上对餐饮消费管理系统进行了设计与实现。')
    
    add_heading_style(doc, 2, '1.1 研究背景')
    add_normal_paragraph(doc, '随着我国高等教育事业的快速发展，高校规模不断扩大，学生数量持续增加。高校餐饮服务作为高校后勤保障的重要组成部分，其管理水平直接影响着师生的日常生活和学校的整体形象。传统的餐饮消费管理方式主要依赖人工操作和纸质记录，存在效率低下、管理困难、数据不准确等问题，已无法满足现代化高校管理的需求。')
    add_normal_paragraph(doc, '在信息化时代背景下，高校信息化建设已成为提升管理水平和服务质量的重要手段。餐饮消费管理系统作为高校信息化建设的重要组成部分，能够实现消费结算的自动化、数据管理的数字化、信息查询的便捷化，为师生提供更加高效、便捷、安全的餐饮服务体验。')
    add_normal_paragraph(doc, '传统的餐饮消费管理方式存在诸多弊端：首先，人工结算方式效率低下，高峰期排队现象严重，影响师生就餐体验；其次，纸质记录容易丢失、损坏，数据统计和分析困难；再次，缺乏有效的账户管理手段，余额查询、充值等操作不够便捷；最后，数据安全性无法得到有效保障，存在信息泄露的风险。', True)
    add_normal_paragraph(doc, '因此，开发一套高效、安全、便捷的餐饮消费管理系统具有重要的现实意义。该系统能够实现消费结算自动化、账户管理智能化、数据统计科学化，为高校餐饮管理提供有力的技术支持，提升高校餐饮服务的整体水平。', True)
    
    add_heading_style(doc, 2, '1.2 发展现状')
    add_normal_paragraph(doc, '国外高校餐饮消费管理系统起步较早，发展较为成熟。早在20世纪80年代，欧美发达国家的高校就开始引入计算机技术进行餐饮消费管理。经过多年的发展，这些系统已经实现了高度的自动化和智能化，能够提供多样化的服务功能，如在线订餐、移动支付、营养分析等。')
    add_normal_paragraph(doc, '在国内，高校餐饮消费管理系统的发展相对较晚，但近年来随着信息技术的快速发展和高校信息化建设的推进，越来越多的高校开始重视餐饮消费管理系统的建设。目前，国内高校餐饮消费管理系统主要呈现以下发展趋势：')
    add_normal_paragraph(doc, '一是系统功能日益完善。现代餐饮消费管理系统不仅具备基本的消费结算功能，还增加了账户管理、充值管理、消费统计、数据分析等功能，能够满足不同用户的需求。', True)
    add_normal_paragraph(doc, '二是移动化趋势明显。随着智能手机的普及，移动支付、手机App查询等功能逐渐成为餐饮消费管理系统的标配，师生可以通过手机随时随地进行消费、查询余额、充值等操作。', True)
    add_normal_paragraph(doc, '三是数据安全受到重视。高校餐饮消费管理系统涉及大量的个人信息和财务数据，数据安全成为系统设计和开发的重要考虑因素。现代系统普遍采用数据加密、访问控制、日志记录等安全措施，确保数据的安全性和完整性。', True)
    add_normal_paragraph(doc, '四是集成化程度提高。餐饮消费管理系统不再是孤立的系统，而是与校园一卡通系统、教务系统、财务系统等进行集成，实现数据共享和业务协同，提升校园信息化的整体水平。', True)
    
    add_heading_style(doc, 2, '1.3 研究意义')
    add_normal_paragraph(doc, '餐饮消费管理系统的研究与开发具有重要的理论意义和实践价值：')
    add_normal_paragraph(doc, '从理论层面来看，本研究将探索如何利用现代信息技术构建高效、安全、便捷的餐饮消费管理系统，为高校信息化建设提供理论参考和实践经验。通过对系统架构、技术选型、数据库设计等方面的研究，丰富高校信息化建设的理论体系。')
    add_normal_paragraph(doc, '从实践层面来看，本研究的成果具有直接的应用价值：', True)
    add_normal_paragraph(doc, '第一，提高餐饮服务效率。通过自动化的消费结算流程，减少人工操作，提高结算速度，缓解就餐高峰期的排队问题，提升师生的就餐体验。', True)
    add_normal_paragraph(doc, '第二，加强财务管理。系统能够实时记录和统计消费数据，为餐饮管理部门提供准确的财务报表和分析数据，帮助管理者及时了解经营状况，做出科学决策。', True)
    add_normal_paragraph(doc, '第三，提升服务质量。系统提供多样化的服务功能，如余额查询、消费记录查询、充值申请等，方便师生随时随地获取服务，提升服务的便捷性和满意度。', True)
    add_normal_paragraph(doc, '第四，保障数据安全。通过完善的安全机制，保护师生的个人信息和财务数据，防止信息泄露和恶意攻击，维护师生的合法权益。', True)
    add_normal_paragraph(doc, '第五，促进校园信息化建设。餐饮消费管理系统作为校园信息化的重要组成部分，与其他系统的集成能够推动校园信息化整体水平的提升，实现资源共享和业务协同。', True)
    
    add_heading_style(doc, 2, '1.4 主要工作')
    add_normal_paragraph(doc, '本项目旨在设计和实现一套完整的餐饮消费管理系统，主要工作包括以下几个方面：')
    add_normal_paragraph(doc, '1、需求分析：通过调研和分析高校餐饮管理的实际需求，明确系统需要实现的功能和性能要求，为系统设计提供依据。')
    add_normal_paragraph(doc, '2、系统设计：根据需求分析的结果，进行系统的总体设计，包括功能模块结构设计、技术架构设计、数据库设计等。', True)
    add_normal_paragraph(doc, '3、技术实现：采用Spring Boot + MyBatis框架进行系统开发，实现学生模块、员工模块、管理员模块等核心功能，确保系统的稳定性和可扩展性。', True)
    add_normal_paragraph(doc, '4、测试与优化：对系统进行全面的功能测试和性能测试，发现并修复存在的问题，优化系统性能，确保系统能够满足实际使用需求。', True)
    add_normal_paragraph(doc, '5、文档编写：编写完整的系统开发文档，包括需求分析文档、设计文档、测试文档等，为系统的维护和扩展提供参考。', True)
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '第2章 需求分析')
    add_normal_paragraph(doc, '需求分析是设计和实现餐饮消费管理系统过程中的基础环节。在此过程中，我们将了解整个系统需要实现哪些功能，需要使用哪些数据，用户对系统的性能有哪些要求。只有在弄清楚系统的需求之后，我们才能寻求实现该系统的解决方案。此阶段是要确定系统功能实现的基础，只有做好需求分析工作，后面的设计与实现将会更加顺利进行。')
    
    add_heading_style(doc, 2, '2.1 性能需求')
    add_normal_paragraph(doc, '本系统的性能需求包括多方面的内容，根据系统的主要用户和关键的应用场景来考虑，这里只对系统的整体性能要求进行了综述，主要包括以下几个方面：')
    add_normal_paragraph(doc, '1、系统响应过程的精确性和及时性：系统响应过程的准确性与及时性是系统实现的第一位要求。响应时间是从用户发出操作请求到该系统响应并开始执行用户操作请求所需的时间，响应时间越短，说明该管理系统的性能越好，效率越高。对于餐饮消费结算等核心操作，响应时间应控制在1秒以内。')
    add_normal_paragraph(doc, '2、系统的可扩展性：系统的扩展性能是非常重要的，它是满足高校餐饮管理与时俱进性的保证。为了系统运行期的平滑升级，开发的技术必须是主流，系统架构必须具有良好的扩展性，能够方便地添加新功能和模块。')
    add_normal_paragraph(doc, '3、系统的易用性与易维护性：餐饮消费管理系统主要面向学生、员工和管理员三类用户，用户群体较为广泛，因此系统必须具有良好的用户界面和简单的操作流程，同时提供相应的提示功能，方便不同层次的用户使用。', True)
    add_normal_paragraph(doc, '4、系统的安全性：随着互联网的飞速发展，系统的安全性越来越被重视，系统的安全性是整个系统的基本保障。餐饮消费管理系统涉及用户的个人信息和财务数据，必须采取有效的安全措施，如数据加密、访问控制、日志记录等，确保数据的安全性和完整性。', True)
    add_normal_paragraph(doc, '5、系统的标准性：系统的研发、运行过程中涉及到很多计算机硬件与软件、数据格式、编码标准等信息都需要使用国际标准或行业标准来定义和使用，确保系统的兼容性和互操作性。', True)
    add_normal_paragraph(doc, '6、系统并发方面的支持：该系统一旦投入运行，同时访问该系统的用户数量可能较多，特别是在就餐高峰期。因此，系统必须具备较好的并发处理能力，能够支持至少500人同时在线使用，确保系统在高并发情况下的稳定性和响应速度。', True)
    
    add_heading_style(doc, 2, '2.2 功能模块需求')
    add_normal_paragraph(doc, '根据高校餐饮消费管理的实际需求，本系统主要分为三个核心模块：学生模块、员工模块和管理员模块。每个模块包含多个子功能，下面将详细介绍各个模块的功能需求。')
    
    add_heading_style(doc, 3, '2.2.1 学生模块需求分析')
    add_normal_paragraph(doc, '学生模块主要面向在校学生用户，提供与餐饮消费相关的各项服务功能。该模块的主要功能需求包括：')
    add_normal_paragraph(doc, '1、用户注册与登录：学生可以通过学号和密码进行注册和登录，系统需要验证用户身份的合法性。')
    add_normal_paragraph(doc, '2、个人信息管理：学生可以查看和修改个人基本信息，包括姓名、院系等，同时可以修改登录密码。')
    add_normal_paragraph(doc, '3、消费记录查询：学生可以查询自己的消费记录，包括消费时间、消费金额、消费地点等信息，并支持按时间范围进行筛选。')
    add_normal_paragraph(doc, '4、余额查询与充值：学生可以查询自己的餐卡余额，并可以通过系统提交充值申请，等待管理员审核。')
    add_normal_paragraph(doc, '5、饭卡挂失与解挂：学生如果丢失饭卡，可以通过系统进行挂失操作，防止他人冒用；找到饭卡后，可以进行解挂操作恢复使用。')
    
    add_heading_style(doc, 3, '2.2.2 员工模块需求分析')
    add_normal_paragraph(doc, '员工模块主要面向餐饮服务人员，提供消费结算和记录查询等功能。该模块的主要功能需求包括：')
    add_normal_paragraph(doc, '1、用户登录：员工可以通过工号和密码进行登录，系统验证身份后进入员工操作界面。')
    add_normal_paragraph(doc, '2、消费结算：员工可以通过扫描学生的饭卡或输入学号进行消费结算，系统自动扣除相应金额并记录消费信息。')
    add_normal_paragraph(doc, '3、今日记录查询：员工可以查询当天的消费记录，包括消费金额、消费人数等统计信息。')
    add_normal_paragraph(doc, '4、历史记录查询：员工可以查询历史消费记录，支持按时间范围和学号进行筛选查询。')
    add_normal_paragraph(doc, '5、密码修改：员工可以修改自己的登录密码，确保账户安全。')
    
    add_heading_style(doc, 3, '2.2.3 管理员模块需求分析')
    add_normal_paragraph(doc, '管理员模块主要面向餐饮管理部门的管理人员，提供系统管理和数据统计等功能。该模块的主要功能需求包括：')
    add_normal_paragraph(doc, '1、用户管理：管理员可以管理学生和员工的信息，包括添加、修改、删除用户信息，重置用户密码等。')
    add_normal_paragraph(doc, '2、充值管理：管理员可以审核学生的充值申请，进行充值操作，并查询充值记录。')
    add_normal_paragraph(doc, '3、消费管理：管理员可以查询所有消费记录，进行数据统计和分析，生成消费报表。')
    add_normal_paragraph(doc, '4、账户管理：管理员可以调整学生的账户余额，处理异常账户问题。')
    add_normal_paragraph(doc, '5、系统统计：管理员可以查看系统的各项统计信息，包括学生人数、员工人数、今日消费总额等。')
    
    doc.add_page_break()
    
    add_normal_paragraph(doc, '为了更清晰地展示系统功能模块的结构，下面列出各个模块的详细功能点：')
    
    student_funcs = [
        ('用户注册', '学生通过学号进行注册，设置初始密码'),
        ('用户登录', '学生通过学号和密码登录系统'),
        ('个人信息查看', '查看个人基本信息和账户余额'),
        ('密码修改', '修改登录密码'),
        ('消费记录查询', '查询历史消费记录，支持时间范围筛选'),
        ('余额查询', '查看当前账户余额'),
        ('充值申请', '提交充值申请，等待审核'),
        ('充值记录查询', '查询充值申请和充值记录'),
        ('饭卡挂失', '挂失丢失的饭卡'),
        ('饭卡解挂', '解除饭卡挂失状态')
    ]
    
    student_table = doc.add_table(rows=len(student_funcs)+1, cols=2)
    student_table.style = 'Table Grid'
    student_table.cell(0, 0).text = '功能名称'
    student_table.cell(0, 1).text = '功能描述'
    for i, (name, desc) in enumerate(student_funcs):
        student_table.cell(i+1, 0).text = name
        student_table.cell(i+1, 1).text = desc
    
    for row in student_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_normal_paragraph(doc, '')
    
    staff_funcs = [
        ('用户登录', '员工通过工号和密码登录系统'),
        ('消费结算', '扫描学生饭卡或输入学号进行消费结算'),
        ('今日记录查询', '查询当天的消费记录和统计信息'),
        ('历史记录查询', '查询历史消费记录，支持筛选'),
        ('密码修改', '修改登录密码')
    ]
    
    staff_table = doc.add_table(rows=len(staff_funcs)+1, cols=2)
    staff_table.style = 'Table Grid'
    staff_table.cell(0, 0).text = '功能名称'
    staff_table.cell(0, 1).text = '功能描述'
    for i, (name, desc) in enumerate(staff_funcs):
        staff_table.cell(i+1, 0).text = name
        staff_table.cell(i+1, 1).text = desc
    
    for row in staff_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_normal_paragraph(doc, '')
    
    admin_funcs = [
        ('用户登录', '管理员通过管理员编号和密码登录系统'),
        ('学生管理', '查看、添加、修改、删除学生信息，重置密码'),
        ('员工管理', '查看、添加、修改、删除员工信息'),
        ('充值审核', '审核学生的充值申请'),
        ('直接充值', '为学生账户直接充值'),
        ('消费记录查询', '查询所有消费记录，支持多条件筛选'),
        ('充值记录查询', '查询所有充值记录'),
        ('余额调整', '调整学生账户余额'),
        ('系统统计', '查看系统各项统计信息')
    ]
    
    admin_table = doc.add_table(rows=len(admin_funcs)+1, cols=2)
    admin_table.style = 'Table Grid'
    admin_table.cell(0, 0).text = '功能名称'
    admin_table.cell(0, 1).text = '功能描述'
    for i, (name, desc) in enumerate(admin_funcs):
        admin_table.cell(i+1, 0).text = name
        admin_table.cell(i+1, 1).text = desc
    
    for row in admin_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 2, '2.3 本章小结')
    add_normal_paragraph(doc, '本章对餐饮消费管理系统的需求分析做了详细的说明，从系统的性能需求出发，阐述了系统在响应时间、可扩展性、易用性、安全性等方面的要求。同时，对学生模块、员工模块和管理员模块的功能需求进行了详细分析，明确了每个模块需要实现的具体功能。这些需求分析为后续的系统设计和实现提供了坚实的基础。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '第3章 总体设计')
    add_normal_paragraph(doc, '餐饮消费管理系统的设计是在前一章需求分析的基础上进行的，对前一章中性能需求和功能需求进行详细的分析和设计，本章内容将从系统的模块结构、系统实现的层次设计、系统数据库设计等几个方面进行详细阐述。')
    
    add_heading_style(doc, 2, '3.1 功能模块结构设计')
    add_normal_paragraph(doc, '根据前一章中的需求分析，我们将餐饮消费管理系统分为三个主要模块：学生模块、员工模块和管理员模块。每个模块包含多个子功能，系统模块结构设计如图3-1所示。')
    add_normal_paragraph(doc, '学生模块主要面向学生用户，提供注册、登录、消费记录查询、充值申请、饭卡挂失等功能；员工模块主要面向餐饮服务人员，提供登录、消费结算、记录查询等功能；管理员模块主要面向管理人员，提供用户管理、充值审核、数据统计等功能。')
    add_normal_paragraph(doc, '图3-1 系统模块结构图')
    add_normal_paragraph(doc, '```mermaid')
    add_normal_paragraph(doc, 'graph TD')
    add_normal_paragraph(doc, '    A[餐饮消费管理系统] --> B[学生模块]')
    add_normal_paragraph(doc, '    A --> C[员工模块]')
    add_normal_paragraph(doc, '    A --> D[管理员模块]')
    add_normal_paragraph(doc, '    B --> B1[注册登录]')
    add_normal_paragraph(doc, '    B --> B2[个人信息]')
    add_normal_paragraph(doc, '    B --> B3[消费记录]')
    add_normal_paragraph(doc, '    B --> B4[充值管理]')
    add_normal_paragraph(doc, '    B --> B5[饭卡管理]')
    add_normal_paragraph(doc, '    C --> C1[登录]')
    add_normal_paragraph(doc, '    C --> C2[消费结算]')
    add_normal_paragraph(doc, '    C --> C3[记录查询]')
    add_normal_paragraph(doc, '    D --> D1[用户管理]')
    add_normal_paragraph(doc, '    D --> D2[充值管理]')
    add_normal_paragraph(doc, '    D --> D3[消费管理]')
    add_normal_paragraph(doc, '    D --> D4[系统统计]')
    add_normal_paragraph(doc, '```')
    
    add_heading_style(doc, 2, '3.2 技术架构设计')
    add_normal_paragraph(doc, '根据软件行业中各种不同框架的比较和分析，我们采用先进的轻量级框架对系统功能进行设计与实现，使用Spring Boot + MyBatis框架作为总体架构。由于考虑到高校餐饮消费数据量较大，信息形式较为复杂，所以对于数据的存储我们使用关系型数据库系统，即MySQL数据库。它是基于客户机/服务器的系统结构，并且具有跨平台移植、分布式数据处理和支持大事务量处理的特点。')
    add_normal_paragraph(doc, 'Spring Boot是一个用于快速构建Java应用程序的框架，它简化了Spring应用的开发过程，提供了自动配置、内嵌服务器等功能，使开发者能够快速搭建一个稳定、高效的应用程序。MyBatis是一个优秀的持久层框架，它支持自定义SQL、存储过程以及高级映射，能够灵活地实现数据访问层的功能。')
    add_normal_paragraph(doc, '前端技术方面，我们采用Thymeleaf模板引擎进行页面渲染，结合HTML5、CSS3和JavaScript实现用户界面的开发。Thymeleaf是一个现代化的服务器端Java模板引擎，它能够无缝地集成到Spring Boot应用中，提供强大的模板处理能力。')
    add_normal_paragraph(doc, '总体技术架构设计如图3-2所示。')
    add_normal_paragraph(doc, '图3-2 总体技术架构设计图')
    
    arch_table = doc.add_table(rows=4, cols=2)
    arch_table.style = 'Table Grid'
    arch_table.cell(0, 0).text = '架构层级'
    arch_table.cell(0, 1).text = '技术实现'
    arch_table.cell(1, 0).text = '表现层'
    arch_table.cell(1, 1).text = 'Thymeleaf + HTML5 + CSS3 + JavaScript'
    arch_table.cell(2, 0).text = '业务逻辑层'
    arch_table.cell(2, 1).text = 'Spring Boot Controller + Service'
    arch_table.cell(3, 0).text = '数据访问层'
    arch_table.cell(3, 1).text = 'MyBatis + MySQL'
    
    for row in arch_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 2, '3.3 技术架构层次设计')
    add_normal_paragraph(doc, '在总体技术架构设计中，包括视图层、控制层、业务逻辑层以及数据访问层等几个层次的设计，系统的开发也将主要集中在这几个层次上进行实现。下面围绕这几个层次进行系统技术架构层次分析。')
    add_normal_paragraph(doc, '1、视图层（View层）')
    add_normal_paragraph(doc, '该餐饮消费管理系统的视图层主要由Thymeleaf模板页面构成，此外还包括HTML5、CSS3、JavaScript等前端技术。Thymeleaf模板引擎能够将服务器端的数据动态渲染到HTML页面中，实现页面的动态展示。CSS3用于页面的样式设计，JavaScript用于实现页面的交互功能，如表单验证、异步请求等。', True)
    add_normal_paragraph(doc, '2、控制层（Controller层）')
    add_normal_paragraph(doc, '控制层主要负责接收用户的请求，并将请求转发给相应的业务逻辑层进行处理。Spring Boot的Controller组件作为控制层的核心，通过@RequestMapping注解定义请求映射，接收HTTP请求并调用Service层的方法进行业务处理，最后将处理结果返回给前端页面。', True)
    add_normal_paragraph(doc, '3、业务逻辑层（Service层）')
    add_normal_paragraph(doc, '业务逻辑层主要用来处理系统具体功能中相对复杂的逻辑关系。该层包含多个Service接口和实现类，每个Service负责处理特定的业务逻辑，如用户管理、消费结算、充值管理等。业务逻辑层通过调用数据访问层来完成数据的存取操作。', True)
    add_normal_paragraph(doc, '4、数据访问层（Mapper层）')
    add_normal_paragraph(doc, '数据访问层专门负责对数据库的交互操作和访问，目的是降低组件耦合度，以屏蔽抽象底层的具体实现。MyBatis通过Mapper接口和XML映射文件实现数据访问，支持灵活的SQL编写和结果映射，能够高效地完成数据库操作。', True)
    
    add_heading_style(doc, 2, '3.4 数据库设计')
    add_normal_paragraph(doc, '数据库设计是系统设计的重要组成部分，它直接影响系统的性能和可维护性。根据需求分析，本系统需要设计以下数据库表：学生信息表、员工信息表、管理员信息表、消费记录表、充值申请表和充值记录表。')
    
    add_heading_style(doc, 3, '3.4.1 学生信息表')
    add_normal_paragraph(doc, '学生信息表用于存储学生的基本信息，包括学号、姓名、院系、密码、余额等字段。')
    
    student_info_table = doc.add_table(rows=9, cols=3)
    student_info_table.style = 'Table Grid'
    student_info_table.cell(0, 0).text = '字段名'
    student_info_table.cell(0, 1).text = '数据类型'
    student_info_table.cell(0, 2).text = '说明'
    student_info_table.cell(1, 0).text = 'student_id'
    student_info_table.cell(1, 1).text = 'VARCHAR(20)'
    student_info_table.cell(1, 2).text = '学号，主键'
    student_info_table.cell(2, 0).text = 'student_name'
    student_info_table.cell(2, 1).text = 'VARCHAR(50)'
    student_info_table.cell(2, 2).text = '学生姓名'
    student_info_table.cell(3, 0).text = 'department'
    student_info_table.cell(3, 1).text = 'VARCHAR(100)'
    student_info_table.cell(3, 2).text = '院系'
    student_info_table.cell(4, 0).text = 'password'
    student_info_table.cell(4, 1).text = 'VARCHAR(100)'
    student_info_table.cell(4, 2).text = '密码'
    student_info_table.cell(5, 0).text = 'balance'
    student_info_table.cell(5, 1).text = 'DECIMAL(10,2)'
    student_info_table.cell(5, 2).text = '余额'
    student_info_table.cell(6, 0).text = 'is_lost'
    student_info_table.cell(6, 1).text = 'INT'
    student_info_table.cell(6, 2).text = '是否挂失：0-正常，1-挂失'
    student_info_table.cell(7, 0).text = 'create_time'
    student_info_table.cell(7, 1).text = 'DATETIME'
    student_info_table.cell(7, 2).text = '创建时间'
    student_info_table.cell(8, 0).text = 'update_time'
    student_info_table.cell(8, 1).text = 'DATETIME'
    student_info_table.cell(8, 2).text = '更新时间'
    
    for row in student_info_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 3, '3.4.2 员工信息表')
    add_normal_paragraph(doc, '员工信息表用于存储餐饮服务人员的基本信息，包括工号、姓名、密码等字段。')
    
    staff_info_table = doc.add_table(rows=6, cols=3)
    staff_info_table.style = 'Table Grid'
    staff_info_table.cell(0, 0).text = '字段名'
    staff_info_table.cell(0, 1).text = '数据类型'
    staff_info_table.cell(0, 2).text = '说明'
    staff_info_table.cell(1, 0).text = 'staff_id'
    staff_info_table.cell(1, 1).text = 'VARCHAR(20)'
    staff_info_table.cell(1, 2).text = '工号，主键'
    staff_info_table.cell(2, 0).text = 'staff_name'
    staff_info_table.cell(2, 1).text = 'VARCHAR(50)'
    staff_info_table.cell(2, 2).text = '员工姓名'
    staff_info_table.cell(3, 0).text = 'password'
    staff_info_table.cell(3, 1).text = 'VARCHAR(100)'
    staff_info_table.cell(3, 2).text = '密码'
    staff_info_table.cell(4, 0).text = 'create_time'
    staff_info_table.cell(4, 1).text = 'DATETIME'
    staff_info_table.cell(4, 2).text = '创建时间'
    staff_info_table.cell(5, 0).text = 'update_time'
    staff_info_table.cell(5, 1).text = 'DATETIME'
    staff_info_table.cell(5, 2).text = '更新时间'
    
    for row in staff_info_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 3, '3.4.3 管理员信息表')
    add_normal_paragraph(doc, '管理员信息表用于存储系统管理员的基本信息，包括管理员编号、姓名、密码等字段。')
    
    admin_info_table = doc.add_table(rows=6, cols=3)
    admin_info_table.style = 'Table Grid'
    admin_info_table.cell(0, 0).text = '字段名'
    admin_info_table.cell(0, 1).text = '数据类型'
    admin_info_table.cell(0, 2).text = '说明'
    admin_info_table.cell(1, 0).text = 'admin_id'
    admin_info_table.cell(1, 1).text = 'VARCHAR(20)'
    admin_info_table.cell(1, 2).text = '管理员编号，主键'
    admin_info_table.cell(2, 0).text = 'admin_name'
    admin_info_table.cell(2, 1).text = 'VARCHAR(50)'
    admin_info_table.cell(2, 2).text = '管理员姓名'
    admin_info_table.cell(3, 0).text = 'password'
    admin_info_table.cell(3, 1).text = 'VARCHAR(100)'
    admin_info_table.cell(3, 2).text = '密码'
    admin_info_table.cell(4, 0).text = 'create_time'
    admin_info_table.cell(4, 1).text = 'DATETIME'
    admin_info_table.cell(4, 2).text = '创建时间'
    admin_info_table.cell(5, 0).text = 'update_time'
    admin_info_table.cell(5, 1).text = 'DATETIME'
    admin_info_table.cell(5, 2).text = '更新时间'
    
    for row in admin_info_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 3, '3.4.4 消费记录表')
    add_normal_paragraph(doc, '消费记录表用于存储学生的消费记录信息，包括记录ID、学号、学生姓名、员工编号、员工姓名、消费金额、消费时间等字段。')
    
    consumption_table = doc.add_table(rows=8, cols=3)
    consumption_table.style = 'Table Grid'
    consumption_table.cell(0, 0).text = '字段名'
    consumption_table.cell(0, 1).text = '数据类型'
    consumption_table.cell(0, 2).text = '说明'
    consumption_table.cell(1, 0).text = 'record_id'
    consumption_table.cell(1, 1).text = 'BIGINT'
    consumption_table.cell(1, 2).text = '记录ID，主键，自增'
    consumption_table.cell(2, 0).text = 'student_id'
    consumption_table.cell(2, 1).text = 'VARCHAR(20)'
    consumption_table.cell(2, 2).text = '学号'
    consumption_table.cell(3, 0).text = 'student_name'
    consumption_table.cell(3, 1).text = 'VARCHAR(50)'
    consumption_table.cell(3, 2).text = '学生姓名'
    consumption_table.cell(4, 0).text = 'staff_id'
    consumption_table.cell(4, 1).text = 'VARCHAR(20)'
    consumption_table.cell(4, 2).text = '员工编号'
    consumption_table.cell(5, 0).text = 'staff_name'
    consumption_table.cell(5, 1).text = 'VARCHAR(50)'
    consumption_table.cell(5, 2).text = '员工姓名'
    consumption_table.cell(6, 0).text = 'amount'
    consumption_table.cell(6, 1).text = 'DECIMAL(10,2)'
    consumption_table.cell(6, 2).text = '消费金额'
    consumption_table.cell(7, 0).text = 'create_time'
    consumption_table.cell(7, 1).text = 'DATETIME'
    consumption_table.cell(7, 2).text = '消费时间'
    
    for row in consumption_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 3, '3.4.5 充值申请表')
    add_normal_paragraph(doc, '充值申请表用于存储学生的充值申请信息，包括申请ID、学号、学生姓名、充值金额、状态、审核管理员编号、审核管理员姓名、申请时间、审核时间等字段。')
    
    recharge_apply_table = doc.add_table(rows=10, cols=3)
    recharge_apply_table.style = 'Table Grid'
    recharge_apply_table.cell(0, 0).text = '字段名'
    recharge_apply_table.cell(0, 1).text = '数据类型'
    recharge_apply_table.cell(0, 2).text = '说明'
    recharge_apply_table.cell(1, 0).text = 'application_id'
    recharge_apply_table.cell(1, 1).text = 'BIGINT'
    recharge_apply_table.cell(1, 2).text = '申请ID，主键，自增'
    recharge_apply_table.cell(2, 0).text = 'student_id'
    recharge_apply_table.cell(2, 1).text = 'VARCHAR(20)'
    recharge_apply_table.cell(2, 2).text = '学号'
    recharge_apply_table.cell(3, 0).text = 'student_name'
    recharge_apply_table.cell(3, 1).text = 'VARCHAR(50)'
    recharge_apply_table.cell(3, 2).text = '学生姓名'
    recharge_apply_table.cell(4, 0).text = 'amount'
    recharge_apply_table.cell(4, 1).text = 'DECIMAL(10,2)'
    recharge_apply_table.cell(4, 2).text = '充值金额'
    recharge_apply_table.cell(5, 0).text = 'status'
    recharge_apply_table.cell(5, 1).text = 'INT'
    recharge_apply_table.cell(5, 2).text = '状态：0-待审核，1-已通过，2-已拒绝'
    recharge_apply_table.cell(6, 0).text = 'admin_id'
    recharge_apply_table.cell(6, 1).text = 'VARCHAR(20)'
    recharge_apply_table.cell(6, 2).text = '审核管理员编号'
    recharge_apply_table.cell(7, 0).text = 'admin_name'
    recharge_apply_table.cell(7, 1).text = 'VARCHAR(50)'
    recharge_apply_table.cell(7, 2).text = '审核管理员姓名'
    recharge_apply_table.cell(8, 0).text = 'apply_time'
    recharge_apply_table.cell(8, 1).text = 'DATETIME'
    recharge_apply_table.cell(8, 2).text = '申请时间'
    recharge_apply_table.cell(9, 0).text = 'audit_time'
    recharge_apply_table.cell(9, 1).text = 'DATETIME'
    recharge_apply_table.cell(9, 2).text = '审核时间'
    
    for row in recharge_apply_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 3, '3.4.6 充值记录表')
    add_normal_paragraph(doc, '充值记录表用于存储学生的充值记录信息，包括记录ID、学号、学生姓名、充值金额、类型、操作人编号、操作人姓名、充值时间等字段。')
    
    recharge_record_table = doc.add_table(rows=9, cols=3)
    recharge_record_table.style = 'Table Grid'
    recharge_record_table.cell(0, 0).text = '字段名'
    recharge_record_table.cell(0, 1).text = '数据类型'
    recharge_record_table.cell(0, 2).text = '说明'
    recharge_record_table.cell(1, 0).text = 'record_id'
    recharge_record_table.cell(1, 1).text = 'BIGINT'
    recharge_record_table.cell(1, 2).text = '记录ID，主键，自增'
    recharge_record_table.cell(2, 0).text = 'student_id'
    recharge_record_table.cell(2, 1).text = 'VARCHAR(20)'
    recharge_record_table.cell(2, 2).text = '学号'
    recharge_record_table.cell(3, 0).text = 'student_name'
    recharge_record_table.cell(3, 1).text = 'VARCHAR(50)'
    recharge_record_table.cell(3, 2).text = '学生姓名'
    recharge_record_table.cell(4, 0).text = 'amount'
    recharge_record_table.cell(4, 1).text = 'DECIMAL(10,2)'
    recharge_record_table.cell(4, 2).text = '充值金额'
    recharge_record_table.cell(5, 0).text = 'type'
    recharge_record_table.cell(5, 1).text = 'INT'
    recharge_record_table.cell(5, 2).text = '类型：0-申请充值，1-直接充值'
    recharge_record_table.cell(6, 0).text = 'operator_id'
    recharge_record_table.cell(6, 1).text = 'VARCHAR(20)'
    recharge_record_table.cell(6, 2).text = '操作人编号'
    recharge_record_table.cell(7, 0).text = 'operator_name'
    recharge_record_table.cell(7, 1).text = 'VARCHAR(50)'
    recharge_record_table.cell(7, 2).text = '操作人姓名'
    recharge_record_table.cell(8, 0).text = 'create_time'
    recharge_record_table.cell(8, 1).text = 'DATETIME'
    recharge_record_table.cell(8, 2).text = '充值时间'
    
    for row in recharge_record_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '3.5 本章小结')
    add_normal_paragraph(doc, '本章主要介绍了餐饮消费管理系统的各个功能模块结构的设计、实现功能模块所需要使用的技术架构、系统层次分析以及各个模块中数据库表结构的设计。该餐饮消费管理系统主要包括学生模块、员工模块和管理员模块等三个主要模块；系统技术架构采用Spring Boot + MyBatis集成框架；系统层次分析从视图层、控制层、业务逻辑层、数据访问层等方面进行探讨；数据库表设计主要阐述了各个模块所需要使用的数据库表结构设计。这些设计为后续的系统实现提供了明确的指导。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '第4章 详细设计及实现')
    add_normal_paragraph(doc, '本章主要根据前面阶段确定下来的系统需求和系统技术架构设计情况，继续进行各个模块功能的详细设计和实现，对主要的业务流程做进一步分析后，为系统的功能编码实现打下坚实的基础。并在系统详细设计的基础上严格按照需求分析所确定下来的功能模块对系统进行详细的编码实现。')
    
    add_heading_style(doc, 2, '4.1 开发环境的搭建')
    add_normal_paragraph(doc, '在开始系统开发之前，需要搭建相应的开发环境。本系统采用Java 21作为开发语言，使用Spring Boot 4.0.6框架进行开发，数据库选用MySQL 8.0+，开发工具使用IntelliJ IDEA。')
    add_normal_paragraph(doc, '1、JDK安装与配置')
    add_normal_paragraph(doc, '首先需要安装Java Development Kit (JDK) 21版本。可以从Oracle官网或OpenJDK官网下载对应的安装包，安装完成后需要配置环境变量，设置JAVA_HOME指向JDK安装目录，并将%JAVA_HOME%\\bin添加到PATH环境变量中。', True)
    add_normal_paragraph(doc, '2、MySQL安装与配置')
    add_normal_paragraph(doc, '安装MySQL 8.0或更高版本，创建数据库实例，并创建名为JavaEE的数据库。设置数据库用户名和密码，确保应用程序能够正常连接到数据库。', True)
    add_normal_paragraph(doc, '3、Maven配置')
    add_normal_paragraph(doc, 'Maven是Java项目的依赖管理工具，需要安装Maven 3.8或更高版本，并配置Maven的settings.xml文件，设置本地仓库路径和镜像源，以提高依赖下载速度。', True)
    add_normal_paragraph(doc, '4、IntelliJ IDEA配置')
    add_normal_paragraph(doc, '安装IntelliJ IDEA开发工具，配置JDK路径和Maven路径，创建新的Spring Boot项目，并导入所需的依赖包。', True)
    
    add_normal_paragraph(doc, '系统的主要依赖包括：')
    dependencies_table = doc.add_table(rows=7, cols=2)
    dependencies_table.style = 'Table Grid'
    dependencies_table.cell(0, 0).text = '依赖名称'
    dependencies_table.cell(0, 1).text = '说明'
    dependencies_table.cell(1, 0).text = 'spring-boot-starter-webmvc'
    dependencies_table.cell(1, 1).text = 'Spring Web MVC支持'
    dependencies_table.cell(2, 0).text = 'spring-boot-starter-thymeleaf'
    dependencies_table.cell(2, 1).text = 'Thymeleaf模板引擎'
    dependencies_table.cell(3, 0).text = 'mybatis-spring-boot-starter'
    dependencies_table.cell(3, 1).text = 'MyBatis集成支持'
    dependencies_table.cell(4, 0).text = 'mysql-connector-j'
    dependencies_table.cell(4, 1).text = 'MySQL数据库驱动'
    dependencies_table.cell(5, 0).text = 'spring-boot-starter-validation'
    dependencies_table.cell(5, 1).text = '数据校验支持'
    dependencies_table.cell(6, 0).text = 'lombok'
    dependencies_table.cell(6, 1).text = '简化Java代码'
    
    for row in dependencies_table.rows:
        for cell in row.cells:
            paragraphs = cell.paragraphs
            for paragraph in paragraphs:
                for run in paragraph.runs:
                    run.font.name = '宋体'
                    run._element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
                    run.font.size = Pt(12)
    
    add_heading_style(doc, 2, '4.2 学生模块的设计与实现')
    add_normal_paragraph(doc, '学生模块是餐饮消费管理系统的核心模块之一，主要面向学生用户提供各项服务功能。该模块的设计与实现包括用户注册、登录、个人信息管理、消费记录查询、充值申请、饭卡挂失等功能。')
    
    add_heading_style(doc, 3, '4.2.1 用户注册功能')
    add_normal_paragraph(doc, '学生用户可以通过注册功能创建自己的账户。注册页面包含学号、姓名、院系、密码等输入项，系统需要验证学号是否已存在，并对密码进行加密存储。')
    add_normal_paragraph(doc, '注册流程如下：')
    add_normal_paragraph(doc, '1、学生访问注册页面，填写学号、姓名、院系、密码等信息；')
    add_normal_paragraph(doc, '2、系统验证学号是否已被注册；')
    add_normal_paragraph(doc, '3、验证通过后，系统将用户信息保存到数据库中；')
    add_normal_paragraph(doc, '4、注册成功后，跳转到登录页面。')
    
    add_heading_style(doc, 3, '4.2.2 用户登录功能')
    add_normal_paragraph(doc, '学生用户可以通过学号和密码登录系统。登录页面包含学号和密码输入框，系统验证用户身份后跳转到学生首页。')
    add_normal_paragraph(doc, '登录流程如下：')
    add_normal_paragraph(doc, '1、学生访问登录页面，输入学号和密码；')
    add_normal_paragraph(doc, '2、系统根据学号查询用户信息，并验证密码是否正确；')
    add_normal_paragraph(doc, '3、验证通过后，跳转到学生首页，显示用户信息和账户余额。')
    
    add_heading_style(doc, 3, '4.2.3 个人信息管理功能')
    add_normal_paragraph(doc, '学生用户可以查看和修改个人信息，包括姓名、院系等基本信息，同时可以修改登录密码。')
    add_normal_paragraph(doc, '个人信息查看流程：')
    add_normal_paragraph(doc, '1、学生登录系统后，点击个人信息菜单；')
    add_normal_paragraph(doc, '2、系统从数据库中查询用户的个人信息；')
    add_normal_paragraph(doc, '3、将查询结果显示在个人信息页面上。')
    
    add_normal_paragraph(doc, '密码修改流程：')
    add_normal_paragraph(doc, '1、学生在个人信息页面点击修改密码按钮；')
    add_normal_paragraph(doc, '2、输入原密码、新密码和确认密码；')
    add_normal_paragraph(doc, '3、系统验证原密码是否正确；')
    add_normal_paragraph(doc, '4、验证通过后，更新用户密码。')
    
    add_heading_style(doc, 3, '4.2.4 消费记录查询功能')
    add_normal_paragraph(doc, '学生用户可以查询自己的消费记录，支持按时间范围进行筛选。')
    add_normal_paragraph(doc, '消费记录查询流程：')
    add_normal_paragraph(doc, '1、学生登录系统后，点击消费记录菜单；')
    add_normal_paragraph(doc, '2、系统从数据库中查询该学生的所有消费记录；')
    add_normal_paragraph(doc, '3、将查询结果分页显示在消费记录页面上；')
    add_normal_paragraph(doc, '4、学生可以输入时间范围进行筛选查询。')
    
    add_heading_style(doc, 3, '4.2.5 充值申请功能')
    add_normal_paragraph(doc, '学生用户可以通过系统提交充值申请，等待管理员审核。')
    add_normal_paragraph(doc, '充值申请流程：')
    add_normal_paragraph(doc, '1、学生登录系统后，点击充值申请菜单；')
    add_normal_paragraph(doc, '2、输入充值金额；')
    add_normal_paragraph(doc, '3、系统将充值申请保存到数据库中，状态设置为待审核；')
    add_normal_paragraph(doc, '4、申请提交成功后，提示用户等待审核。')
    
    add_heading_style(doc, 3, '4.2.6 饭卡挂失与解挂功能')
    add_normal_paragraph(doc, '学生用户如果丢失饭卡，可以通过系统进行挂失操作，防止他人冒用；找到饭卡后，可以进行解挂操作恢复使用。')
    add_normal_paragraph(doc, '饭卡挂失流程：')
    add_normal_paragraph(doc, '1、学生登录系统后，点击饭卡挂失按钮；')
    add_normal_paragraph(doc, '2、系统更新学生账户的挂失状态为挂失；')
    add_normal_paragraph(doc, '3、挂失成功后，该账户将无法进行消费操作。')
    
    add_normal_paragraph(doc, '饭卡解挂流程：')
    add_normal_paragraph(doc, '1、学生登录系统后，点击饭卡解挂按钮；')
    add_normal_paragraph(doc, '2、系统更新学生账户的挂失状态为正常；')
    add_normal_paragraph(doc, '3、解挂成功后，该账户可以正常进行消费操作。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '4.3 员工模块的设计与实现')
    add_normal_paragraph(doc, '员工模块主要面向餐饮服务人员，提供消费结算和记录查询等功能。该模块的设计与实现包括用户登录、消费结算、今日记录查询、历史记录查询、密码修改等功能。')
    
    add_heading_style(doc, 3, '4.3.1 用户登录功能')
    add_normal_paragraph(doc, '员工用户可以通过工号和密码登录系统。登录页面包含工号和密码输入框，系统验证用户身份后跳转到员工首页。')
    add_normal_paragraph(doc, '登录流程如下：')
    add_normal_paragraph(doc, '1、员工访问登录页面，输入工号和密码；')
    add_normal_paragraph(doc, '2、系统根据工号查询用户信息，并验证密码是否正确；')
    add_normal_paragraph(doc, '3、验证通过后，跳转到员工首页，显示员工信息。')
    
    add_heading_style(doc, 3, '4.3.2 消费结算功能')
    add_normal_paragraph(doc, '员工用户可以通过扫描学生的饭卡或输入学号进行消费结算，系统自动扣除相应金额并记录消费信息。')
    add_normal_paragraph(doc, '消费结算流程：')
    add_normal_paragraph(doc, '1、员工登录系统后，进入消费结算页面；')
    add_normal_paragraph(doc, '2、输入学生学号或扫描饭卡；')
    add_normal_paragraph(doc, '3、系统查询学生信息和账户余额；')
    add_normal_paragraph(doc, '4、输入消费金额；')
    add_normal_paragraph(doc, '5、系统验证学生账户余额是否充足；')
    add_normal_paragraph(doc, '6、余额充足时，扣除相应金额并记录消费信息；')
    add_normal_paragraph(doc, '7、显示消费成功信息。')
    
    add_heading_style(doc, 3, '4.3.3 今日记录查询功能')
    add_normal_paragraph(doc, '员工用户可以查询当天的消费记录，包括消费金额、消费人数等统计信息。')
    add_normal_paragraph(doc, '今日记录查询流程：')
    add_normal_paragraph(doc, '1、员工登录系统后，点击今日记录菜单；')
    add_normal_paragraph(doc, '2、系统查询当天该员工的所有消费记录；')
    add_normal_paragraph(doc, '3、统计消费总金额和消费人数；')
    add_normal_paragraph(doc, '4、将查询结果显示在今日记录页面上。')
    
    add_heading_style(doc, 3, '4.3.4 历史记录查询功能')
    add_normal_paragraph(doc, '员工用户可以查询历史消费记录，支持按时间范围和学号进行筛选查询。')
    add_normal_paragraph(doc, '历史记录查询流程：')
    add_normal_paragraph(doc, '1、员工登录系统后，点击历史记录菜单；')
    add_normal_paragraph(doc, '2、输入时间范围或学号进行筛选；')
    add_normal_paragraph(doc, '3、系统根据筛选条件查询消费记录；')
    add_normal_paragraph(doc, '4、将查询结果分页显示在历史记录页面上。')
    
    add_heading_style(doc, 3, '4.3.5 密码修改功能')
    add_normal_paragraph(doc, '员工用户可以修改自己的登录密码，确保账户安全。')
    add_normal_paragraph(doc, '密码修改流程：')
    add_normal_paragraph(doc, '1、员工登录系统后，点击修改密码菜单；')
    add_normal_paragraph(doc, '2、输入原密码、新密码和确认密码；')
    add_normal_paragraph(doc, '3、系统验证原密码是否正确；')
    add_normal_paragraph(doc, '4、验证通过后，更新用户密码。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '4.4 管理员模块的设计与实现')
    add_normal_paragraph(doc, '管理员模块主要面向餐饮管理部门的管理人员，提供系统管理和数据统计等功能。该模块的设计与实现包括用户登录、学生管理、员工管理、充值审核、直接充值、消费记录查询、充值记录查询、余额调整、系统统计等功能。')
    
    add_heading_style(doc, 3, '4.4.1 用户登录功能')
    add_normal_paragraph(doc, '管理员用户可以通过管理员编号和密码登录系统。登录页面包含管理员编号和密码输入框，系统验证用户身份后跳转到管理员首页。')
    add_normal_paragraph(doc, '登录流程如下：')
    add_normal_paragraph(doc, '1、管理员访问登录页面，输入管理员编号和密码；')
    add_normal_paragraph(doc, '2、系统根据管理员编号查询用户信息，并验证密码是否正确；')
    add_normal_paragraph(doc, '3、验证通过后，跳转到管理员首页，显示系统统计信息。')
    
    add_heading_style(doc, 3, '4.4.2 学生管理功能')
    add_normal_paragraph(doc, '管理员可以管理学生信息，包括查看、添加、修改、删除学生信息，重置学生密码等功能。')
    add_normal_paragraph(doc, '学生列表查看流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击学生管理菜单；')
    add_normal_paragraph(doc, '2、系统查询所有学生信息；')
    add_normal_paragraph(doc, '3、将查询结果分页显示在学生列表页面上。')
    
    add_normal_paragraph(doc, '学生信息添加流程：')
    add_normal_paragraph(doc, '1、管理员在学生列表页面点击添加按钮；')
    add_normal_paragraph(doc, '2、填写学生学号、姓名、院系等信息；')
    add_normal_paragraph(doc, '3、系统验证学号是否已存在；')
    add_normal_paragraph(doc, '4、验证通过后，保存学生信息到数据库。')
    
    add_normal_paragraph(doc, '学生信息修改流程：')
    add_normal_paragraph(doc, '1、管理员在学生列表页面点击修改按钮；')
    add_normal_paragraph(doc, '2、系统查询该学生的详细信息并显示；')
    add_normal_paragraph(doc, '3、修改学生信息；')
    add_normal_paragraph(doc, '4、保存修改后的信息到数据库。')
    
    add_normal_paragraph(doc, '学生信息删除流程：')
    add_normal_paragraph(doc, '1、管理员在学生列表页面选中需要删除的学生；')
    add_normal_paragraph(doc, '2、点击删除按钮；')
    add_normal_paragraph(doc, '3、系统删除该学生信息。')
    
    add_normal_paragraph(doc, '学生密码重置流程：')
    add_normal_paragraph(doc, '1、管理员在学生列表页面选中需要重置密码的学生；')
    add_normal_paragraph(doc, '2、点击重置密码按钮；')
    add_normal_paragraph(doc, '3、系统将学生密码重置为默认密码。')
    
    add_heading_style(doc, 3, '4.4.3 员工管理功能')
    add_normal_paragraph(doc, '管理员可以管理员工信息，包括查看、添加、修改、删除员工信息等功能。')
    add_normal_paragraph(doc, '员工列表查看流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击员工管理菜单；')
    add_normal_paragraph(doc, '2、系统查询所有员工信息；')
    add_normal_paragraph(doc, '3、将查询结果分页显示在员工列表页面上。')
    
    add_normal_paragraph(doc, '员工信息添加流程：')
    add_normal_paragraph(doc, '1、管理员在员工列表页面点击添加按钮；')
    add_normal_paragraph(doc, '2、填写员工工号、姓名等信息；')
    add_normal_paragraph(doc, '3、系统验证工号是否已存在；')
    add_normal_paragraph(doc, '4、验证通过后，保存员工信息到数据库。')
    
    add_normal_paragraph(doc, '员工信息修改流程：')
    add_normal_paragraph(doc, '1、管理员在员工列表页面点击修改按钮；')
    add_normal_paragraph(doc, '2、系统查询该员工的详细信息并显示；')
    add_normal_paragraph(doc, '3、修改员工信息；')
    add_normal_paragraph(doc, '4、保存修改后的信息到数据库。')
    
    add_normal_paragraph(doc, '员工信息删除流程：')
    add_normal_paragraph(doc, '1、管理员在员工列表页面选中需要删除的员工；')
    add_normal_paragraph(doc, '2、点击删除按钮；')
    add_normal_paragraph(doc, '3、系统删除该员工信息。')
    
    add_heading_style(doc, 3, '4.4.4 充值审核功能')
    add_normal_paragraph(doc, '管理员可以审核学生的充值申请，决定是否通过申请。')
    add_normal_paragraph(doc, '充值审核流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击充值申请菜单；')
    add_normal_paragraph(doc, '2、系统查询所有待审核的充值申请；')
    add_normal_paragraph(doc, '3、管理员查看申请详情；')
    add_normal_paragraph(doc, '4、选择通过或拒绝申请；')
    add_normal_paragraph(doc, '5、如果通过，系统增加学生账户余额并记录充值记录；')
    add_normal_paragraph(doc, '6、更新申请状态为已通过或已拒绝。')
    
    add_heading_style(doc, 3, '4.4.5 直接充值功能')
    add_normal_paragraph(doc, '管理员可以直接为学生账户充值，无需经过申请审核流程。')
    add_normal_paragraph(doc, '直接充值流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击直接充值菜单；')
    add_normal_paragraph(doc, '2、输入学生学号查询学生信息；')
    add_normal_paragraph(doc, '3、输入充值金额；')
    add_normal_paragraph(doc, '4、系统增加学生账户余额；')
    add_normal_paragraph(doc, '5、记录充值记录。')
    
    add_heading_style(doc, 3, '4.4.6 消费记录查询功能')
    add_normal_paragraph(doc, '管理员可以查询所有消费记录，支持按学生学号、员工编号、时间范围等条件进行筛选。')
    add_normal_paragraph(doc, '消费记录查询流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击消费记录菜单；')
    add_normal_paragraph(doc, '2、输入筛选条件；')
    add_normal_paragraph(doc, '3、系统根据条件查询消费记录；')
    add_normal_paragraph(doc, '4、将查询结果分页显示在消费记录页面上。')
    
    add_heading_style(doc, 3, '4.4.7 充值记录查询功能')
    add_normal_paragraph(doc, '管理员可以查询所有充值记录，支持按学生学号、操作人编号、时间范围等条件进行筛选。')
    add_normal_paragraph(doc, '充值记录查询流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击充值记录菜单；')
    add_normal_paragraph(doc, '2、输入筛选条件；')
    add_normal_paragraph(doc, '3、系统根据条件查询充值记录；')
    add_normal_paragraph(doc, '4、将查询结果分页显示在充值记录页面上。')
    
    add_heading_style(doc, 3, '4.4.8 余额调整功能')
    add_normal_paragraph(doc, '管理员可以调整学生的账户余额，处理异常账户问题。')
    add_normal_paragraph(doc, '余额调整流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，点击余额调整菜单；')
    add_normal_paragraph(doc, '2、输入学生学号查询学生信息；')
    add_normal_paragraph(doc, '3、输入调整金额（正数为增加，负数为减少）；')
    add_normal_paragraph(doc, '4、系统更新学生账户余额；')
    add_normal_paragraph(doc, '5、记录余额调整操作。')
    
    add_heading_style(doc, 3, '4.4.9 系统统计功能')
    add_normal_paragraph(doc, '管理员可以查看系统的各项统计信息，包括学生人数、员工人数、今日消费总额等。')
    add_normal_paragraph(doc, '系统统计流程：')
    add_normal_paragraph(doc, '1、管理员登录系统后，系统自动统计各项信息；')
    add_normal_paragraph(doc, '2、在管理员首页显示统计结果；')
    add_normal_paragraph(doc, '3、管理员可以点击统计报表菜单查看详细统计信息。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '4.5 本章小结')
    add_normal_paragraph(doc, '本章详细介绍了餐饮消费管理系统各个模块的设计与实现过程。从开发环境的搭建开始，介绍了系统所需的开发工具和依赖配置。随后详细阐述了学生模块、员工模块和管理员模块的各个功能的设计与实现流程，包括用户注册登录、个人信息管理、消费记录查询、充值申请、饭卡挂失、消费结算、用户管理、充值审核等功能。这些详细的设计与实现过程为系统的开发提供了明确的指导。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '第5章 测试')
    add_normal_paragraph(doc, '系统功能实现完善后，下面将对系统的每一个功能进行测试，确保每一个功能的实现符合逻辑，符合需求设定。下面将详细介绍对每一个功能的测试。')
    
    add_heading_style(doc, 2, '5.1 学生模块功能测试')
    add_normal_paragraph(doc, '1、用户注册功能测试')
    add_normal_paragraph(doc, '测试步骤：访问学生注册页面，输入学号、姓名、院系、密码等信息，点击注册按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证学号是否已存在，若不存在则注册成功并跳转到登录页面；若已存在则提示学号已被注册。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '2、用户登录功能测试')
    add_normal_paragraph(doc, '测试步骤：访问学生登录页面，输入学号和密码，点击登录按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证学号和密码是否正确，正确则跳转到学生首页；错误则提示学号或密码错误。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '3、个人信息查看功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击个人信息菜单。')
    add_normal_paragraph(doc, '预期结果：页面显示学生的个人信息和账户余额。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '4、密码修改功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击修改密码按钮，输入原密码、新密码和确认密码，点击确定按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证原密码是否正确，正确则修改密码成功；错误则提示原密码错误。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '5、消费记录查询功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击消费记录菜单，输入时间范围进行筛选。')
    add_normal_paragraph(doc, '预期结果：页面显示该学生的消费记录，支持按时间范围筛选。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '6、充值申请功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击充值申请菜单，输入充值金额，点击提交按钮。')
    add_normal_paragraph(doc, '预期结果：系统保存充值申请，状态为待审核，提示申请成功。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '7、饭卡挂失与解挂功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击饭卡挂失按钮；之后点击饭卡解挂按钮。')
    add_normal_paragraph(doc, '预期结果：挂失后账户无法消费，解挂后账户恢复正常消费功能。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '5.2 员工模块功能测试')
    add_normal_paragraph(doc, '1、用户登录功能测试')
    add_normal_paragraph(doc, '测试步骤：访问员工登录页面，输入工号和密码，点击登录按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证工号和密码是否正确，正确则跳转到员工首页；错误则提示工号或密码错误。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '2、消费结算功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，进入消费结算页面，输入学生学号，查询学生信息，输入消费金额，点击结算按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证学生账户余额是否充足，充足则扣除金额并记录消费；不足则提示余额不足。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '3、今日记录查询功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击今日记录菜单。')
    add_normal_paragraph(doc, '预期结果：页面显示当天该员工的消费记录和统计信息。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '4、历史记录查询功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击历史记录菜单，输入时间范围或学号进行筛选。')
    add_normal_paragraph(doc, '预期结果：页面显示符合条件的消费记录。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '5、密码修改功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击修改密码按钮，输入原密码、新密码和确认密码，点击确定按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证原密码是否正确，正确则修改密码成功；错误则提示原密码错误。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '5.3 管理员模块功能测试')
    add_normal_paragraph(doc, '1、用户登录功能测试')
    add_normal_paragraph(doc, '测试步骤：访问管理员登录页面，输入管理员编号和密码，点击登录按钮。')
    add_normal_paragraph(doc, '预期结果：系统验证管理员编号和密码是否正确，正确则跳转到管理员首页；错误则提示编号或密码错误。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '2、学生管理功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击学生管理菜单，执行添加、修改、删除、重置密码等操作。')
    add_normal_paragraph(doc, '预期结果：各项操作均能正常执行，数据正确保存到数据库。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '3、员工管理功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击员工管理菜单，执行添加、修改、删除等操作。')
    add_normal_paragraph(doc, '预期结果：各项操作均能正常执行，数据正确保存到数据库。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '4、充值审核功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击充值申请菜单，选择待审核的申请，点击通过或拒绝按钮。')
    add_normal_paragraph(doc, '预期结果：通过则增加学生账户余额并记录充值记录；拒绝则更新申请状态为已拒绝。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '5、直接充值功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击直接充值菜单，输入学生学号，查询学生信息，输入充值金额，点击充值按钮。')
    add_normal_paragraph(doc, '预期结果：系统增加学生账户余额并记录充值记录。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '6、消费记录查询功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击消费记录菜单，输入筛选条件进行查询。')
    add_normal_paragraph(doc, '预期结果：页面显示符合条件的消费记录。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '7、充值记录查询功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击充值记录菜单，输入筛选条件进行查询。')
    add_normal_paragraph(doc, '预期结果：页面显示符合条件的充值记录。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '8、余额调整功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，点击余额调整菜单，输入学生学号，查询学生信息，输入调整金额，点击确定按钮。')
    add_normal_paragraph(doc, '预期结果：系统更新学生账户余额。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    add_normal_paragraph(doc, '9、系统统计功能测试')
    add_normal_paragraph(doc, '测试步骤：登录系统后，查看管理员首页的统计信息。')
    add_normal_paragraph(doc, '预期结果：页面显示学生人数、员工人数、今日消费总额等统计信息。')
    add_normal_paragraph(doc, '测试结果：通过', True)
    
    doc.add_page_break()
    
    add_heading_style(doc, 2, '5.4 本章小结')
    add_normal_paragraph(doc, '本章主要介绍了对餐饮消费管理系统各个模块中每一个功能进行详细的测试，阐述了执行什么操作，需要达到什么样的效果，表示此功能测试成功。测试结果表明，系统的所有功能均能正常运行，符合需求分析的要求。对于测试过程中发现的问题，已经及时进行了修复和优化，确保系统能够稳定、可靠地运行。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '总  结')
    add_normal_paragraph(doc, '本文运用Spring Boot + MyBatis集成架构，构建了餐饮消费管理系统，该系统经过良好的测试，功能实现健全，相信以后会为高校餐饮管理带来良好的经济效益和管理效益。')
    add_normal_paragraph(doc, '本文主要从需求分析、系统概要设计、系统详细设计与实现和系统测试等几个方面详细描述。首先，在需求分析中详细介绍了各个模块需要实现怎样的功能；在系统概要设计中介绍了系统的结构设计图，以及整个项目用到的技术架构，系统中各个层次之间的关系等内容；在系统详细设计与实现中展示了系统中的主要界面设计，另外还详细介绍了各个功能实现的业务逻辑；在系统运行与测试部分中详细介绍了系统功能怎样显示，表示此功能测试成功。')
    add_normal_paragraph(doc, '总之，餐饮消费管理系统已经实现了大部分功能，包括学生模块、员工模块和管理员模块的各项功能。系统具有良好的用户界面和操作流程，能够满足高校餐饮管理的实际需求。同时，系统还具有较好的扩展性和维护性，为后续的功能扩展和系统升级提供了良好的基础。')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '参考文献')
    add_normal_paragraph(doc, '[1] 王卫红. Spring Boot实战[M]. 北京：机械工业出版社，2021.')
    add_normal_paragraph(doc, '[2] 刘增辉. MyBatis从入门到精通[M]. 北京：电子工业出版社，2020.')
    add_normal_paragraph(doc, '[3] 李刚. Java EE企业级应用开发[M]. 北京：清华大学出版社，2022.')
    add_normal_paragraph(doc, '[4] 陈惠贞. 数据库系统原理与应用[M]. 北京：人民邮电出版社，2021.')
    add_normal_paragraph(doc, '[5] 张桂元. 软件工程导论[M]. 北京：清华大学出版社，2020.')
    add_normal_paragraph(doc, '[6] 周志华. 系统架构设计实践[M]. 北京：机械工业出版社，2021.')
    add_normal_paragraph(doc, '[7] 赵强. Web应用开发技术[M]. 北京：电子工业出版社，2022.')
    add_normal_paragraph(doc, '[8] 孙卫琴. Java编程思想[M]. 北京：机械工业出版社，2020.')
    
    doc.add_page_break()
    
    add_heading_style(doc, 1, '附  录')
    add_normal_paragraph(doc, '附录A：项目目录结构')
    add_normal_paragraph(doc, '```')
    add_normal_paragraph(doc, 'DiningExpenseManagementSystem/')
    add_normal_paragraph(doc, '├── src/')
    add_normal_paragraph(doc, '│   └── main/')
    add_normal_paragraph(doc, '│       ├── java/')
    add_normal_paragraph(doc, '│       │   └── com/hgnu/diningexpensemanagementsystem/')
    add_normal_paragraph(doc, '│       │       ├── controller/')
    add_normal_paragraph(doc, '│       │       ├── service/')
    add_normal_paragraph(doc, '│       │       ├── mapper/')
    add_normal_paragraph(doc, '│       │       ├── entity/')
    add_normal_paragraph(doc, '│       │       └── DiningExpenseManagementSystemApplication.java')
    add_normal_paragraph(doc, '│       └── resources/')
    add_normal_paragraph(doc, '│           ├── mapper/')
    add_normal_paragraph(doc, '│           ├── templates/')
    add_normal_paragraph(doc, '│           ├── application.properties')
    add_normal_paragraph(doc, '│           ├── schema.sql')
    add_normal_paragraph(doc, '│           └── data.sql')
    add_normal_paragraph(doc, '├── pom.xml')
    add_normal_paragraph(doc, '└── README.md')
    add_normal_paragraph(doc, '```')
    
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, '附录B：数据库初始化脚本')
    add_normal_paragraph(doc, '```sql')
    add_normal_paragraph(doc, 'CREATE TABLE student (')
    add_normal_paragraph(doc, '    student_id VARCHAR(20) PRIMARY KEY,')
    add_normal_paragraph(doc, '    student_name VARCHAR(50) NOT NULL,')
    add_normal_paragraph(doc, '    department VARCHAR(100),')
    add_normal_paragraph(doc, '    password VARCHAR(100) NOT NULL,')
    add_normal_paragraph(doc, '    balance DECIMAL(10,2) DEFAULT 0,')
    add_normal_paragraph(doc, '    is_lost INT DEFAULT 0,')
    add_normal_paragraph(doc, '    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,')
    add_normal_paragraph(doc, '    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, 'CREATE TABLE staff (')
    add_normal_paragraph(doc, '    staff_id VARCHAR(20) PRIMARY KEY,')
    add_normal_paragraph(doc, '    staff_name VARCHAR(50) NOT NULL,')
    add_normal_paragraph(doc, '    password VARCHAR(100) NOT NULL,')
    add_normal_paragraph(doc, '    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,')
    add_normal_paragraph(doc, '    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, 'CREATE TABLE admin (')
    add_normal_paragraph(doc, '    admin_id VARCHAR(20) PRIMARY KEY,')
    add_normal_paragraph(doc, '    admin_name VARCHAR(50) NOT NULL,')
    add_normal_paragraph(doc, '    password VARCHAR(100) NOT NULL,')
    add_normal_paragraph(doc, '    create_time DATETIME DEFAULT CURRENT_TIMESTAMP,')
    add_normal_paragraph(doc, '    update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, 'CREATE TABLE consumption_record (')
    add_normal_paragraph(doc, '    record_id BIGINT PRIMARY KEY AUTO_INCREMENT,')
    add_normal_paragraph(doc, '    student_id VARCHAR(20),')
    add_normal_paragraph(doc, '    student_name VARCHAR(50),')
    add_normal_paragraph(doc, '    staff_id VARCHAR(20),')
    add_normal_paragraph(doc, '    staff_name VARCHAR(50),')
    add_normal_paragraph(doc, '    amount DECIMAL(10,2) NOT NULL,')
    add_normal_paragraph(doc, '    create_time DATETIME DEFAULT CURRENT_TIMESTAMP')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, 'CREATE TABLE recharge_application (')
    add_normal_paragraph(doc, '    application_id BIGINT PRIMARY KEY AUTO_INCREMENT,')
    add_normal_paragraph(doc, '    student_id VARCHAR(20),')
    add_normal_paragraph(doc, '    student_name VARCHAR(50),')
    add_normal_paragraph(doc, '    amount DECIMAL(10,2) NOT NULL,')
    add_normal_paragraph(doc, '    status INT DEFAULT 0,')
    add_normal_paragraph(doc, '    admin_id VARCHAR(20),')
    add_normal_paragraph(doc, '    admin_name VARCHAR(50),')
    add_normal_paragraph(doc, '    apply_time DATETIME DEFAULT CURRENT_TIMESTAMP,')
    add_normal_paragraph(doc, '    audit_time DATETIME')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '')
    add_normal_paragraph(doc, 'CREATE TABLE recharge_record (')
    add_normal_paragraph(doc, '    record_id BIGINT PRIMARY KEY AUTO_INCREMENT,')
    add_normal_paragraph(doc, '    student_id VARCHAR(20),')
    add_normal_paragraph(doc, '    student_name VARCHAR(50),')
    add_normal_paragraph(doc, '    amount DECIMAL(10,2) NOT NULL,')
    add_normal_paragraph(doc, '    type INT DEFAULT 0,')
    add_normal_paragraph(doc, '    operator_id VARCHAR(20),')
    add_normal_paragraph(doc, '    operator_name VARCHAR(50),')
    add_normal_paragraph(doc, '    create_time DATETIME DEFAULT CURRENT_TIMESTAMP')
    add_normal_paragraph(doc, ');')
    add_normal_paragraph(doc, '```')
    
    doc.save('软件开发文档.docx')
    print('文档生成成功！')

if __name__ == '__main__':
    create_document()
