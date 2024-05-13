# Generated by Django 4.1 on 2024-05-13 19:47

import ckeditor.fields
import config.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import store.models


class Migration(migrations.Migration):
    dependencies = [
        ("brand", "0002_alter_brand_options_alter_brand_logo_and_more"),
        ("gallery", "0002_alter_gallery_options_alter_gallery_image_and_more"),
        ("address", "0003_alter_address_options_alter_address_city_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "discount",
            "0002_alter_discountcode_options_alter_discountcode_code_and_more",
        ),
        ("store", "0017_paymentmethod_price_per_kilo_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "دسته محصولات",
                "verbose_name_plural": "دسته های محصولات",
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "نظر", "verbose_name_plural": "نظرات"},
        ),
        migrations.AlterModelOptions(
            name="favoriteproduct",
            options={
                "verbose_name": "مورد علاقه",
                "verbose_name_plural": "مورد علاقه ها",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={"verbose_name": "سفارش", "verbose_name_plural": "سفارش ها"},
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={
                "verbose_name": "آیتم سفارش",
                "verbose_name_plural": "آیتم های سفارش",
            },
        ),
        migrations.AlterModelOptions(
            name="paymentmethod",
            options={
                "verbose_name": "روش پرداخت",
                "verbose_name_plural": "روش های پرداخت",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "محصول", "verbose_name_plural": "محصولات"},
        ),
        migrations.AlterModelOptions(
            name="specifications",
            options={
                "verbose_name": "مشخصه محصول",
                "verbose_name_plural": "مشخصات محصولات",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="is_cart",
            field=models.BooleanField(
                default=False, verbose_name="نمایش به صورت کارتی ؟"
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=store.models.category_logo_file_path,
                verbose_name="لوگو",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="order",
            field=models.IntegerField(default=1, verbose_name="الویت نمایش"),
        ),
        migrations.AlterField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_categories",
                to="store.category",
                verbose_name="دسته پدر",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=72, verbose_name="عنوان"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="create_data",
            field=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="full_name",
            field=models.CharField(max_length=125, verbose_name="نام کامل"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="وضعیت"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="store.product",
                verbose_name="محصول",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.CharField(max_length=750, verbose_name="متن"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
        migrations.AlterField(
            model_name="favoriteproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorited_by",
                to="store.product",
                verbose_name="محصول",
            ),
        ),
        migrations.AlterField(
            model_name="favoriteproduct",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_products",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="orders",
                to="address.address",
                verbose_name="نشانی",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="code",
            field=models.CharField(max_length=225, null=True, verbose_name="کد سفارش"),
        ),
        migrations.AlterField(
            model_name="order",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="orders",
                to="discount.discountcode",
                verbose_name="تخفیف",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="orders",
                to="store.paymentmethod",
                verbose_name="روش پرداخت",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(
                max_length=11,
                validators=[config.validators.PhoneValidator],
                verbose_name="موبایل",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="state",
            field=models.CharField(
                choices=[
                    ("P", "در انتظار بررسی (پرداخت شده)"),
                    ("D", "تکمیل شده"),
                    ("C", "لغو شده / پر داخت ناموفق"),
                    ("DD", "در دست اقدام"),
                ],
                default="P",
                max_length=2,
                verbose_name="وضعیت",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=0,
                default_currency="IRR",
                max_digits=10,
                verbose_name="قیمت کل",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="کاربر",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="brand",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="برند"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="count",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="تعداد",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="store.order",
                verbose_name="سفارش",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=0,
                default_currency="IRR",
                max_digits=10,
                null=True,
                verbose_name="قیمت",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product_id",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="شناسه محصول"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="technical_number",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="کد فنی"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="title",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="عنوان"
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=0,
                default_currency="IRR",
                max_digits=10,
                verbose_name="هزینه",
            ),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="title",
            field=models.CharField(max_length=125, verbose_name="عنوان"),
        ),
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="brand.brand",
                verbose_name="برند",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="store.category",
                verbose_name="دسته",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="count",
            field=models.IntegerField(default=0, verbose_name="موجودی انبار"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
        ),
        migrations.AlterField(
            model_name="product",
            name="desc",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="توضیحات"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="gallery",
            field=models.ManyToManyField(
                related_name="products", to="gallery.gallery", verbose_name="گالری"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="order_count",
            field=models.IntegerField(default=0, verbose_name="تعداد سفارش"),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=0,
                default_currency="IRR",
                max_digits=12,
                verbose_name="قیمت",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="short_desc",
            field=models.CharField(
                blank=True, max_length=300, null=True, verbose_name="توضیحات کوتاه"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="technical_number",
            field=models.CharField(
                blank=True, max_length=125, null=True, verbose_name="کد فنی"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=125, verbose_name="عنوان"),
        ),
        migrations.AlterField(
            model_name="product",
            name="weight",
            field=models.FloatField(default=0, verbose_name="وزن (کیلو گرم)"),
        ),
        migrations.AlterField(
            model_name="specifications",
            name="key",
            field=models.CharField(max_length=125, verbose_name="مشخصه"),
        ),
        migrations.AlterField(
            model_name="specifications",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="specs",
                to="store.product",
                verbose_name="محصول",
            ),
        ),
        migrations.AlterField(
            model_name="specifications",
            name="value",
            field=models.CharField(max_length=225, verbose_name="مقدار"),
        ),
        migrations.DeleteModel(
            name="FavoriteProductList",
        ),
    ]