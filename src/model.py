"""
Medical Image Analysis Model
This module will contain the trained model for chest X-ray classification.
"""

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import DenseNet121

class ChestXRayClassifier:
    """
    Chest X-ray classifier for medical image analysis.
    
    Detects:
    - Normal
    - Pneumonia
    - COVID-19
    - Tuberculosis
    """
    
    def __init__(self, num_classes=4, input_shape=(224, 224, 3)):
        self.num_classes = num_classes
        self.input_shape = input_shape
        self.model = None
        
    def build_model(self):
        """Build the classification model"""
        # Base model
        base_model = DenseNet121(
            weights='imagenet',
            include_top=False,
            input_shape=self.input_shape
        )
        
        # Freeze base layers
        base_model.trainable = False
        
        # Build full model
        inputs = layers.Input(shape=self.input_shape)
        x = base_model(inputs, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(256, activation='relu')(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(self.num_classes, activation='softmax')(x)
        
        self.model = models.Model(inputs, outputs)
        
        return self.model
    
    def compile_model(self, learning_rate=0.001):
        """Compile the model"""
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy', 'AUC']
        )
        
    def train(self, train_data, val_data, epochs=20):
        """Train the model"""
        history = self.model.fit(
            train_data,
            validation_data=val_data,
            epochs=epochs,
            callbacks=[
                tf.keras.callbacks.EarlyStopping(patience=5),
                tf.keras.callbacks.ModelCheckpoint('best_model.h5', save_best_only=True)
            ]
        )
        return history
    
    def predict(self, image):
        """Make predictions on a single image"""
        predictions = self.model.predict(image)
        return predictions
    
    def save(self, filepath):
        """Save model to file"""
        self.model.save(filepath)
        
    def load(self, filepath):
        """Load model from file"""
        self.model = tf.keras.models.load_model(filepath)
